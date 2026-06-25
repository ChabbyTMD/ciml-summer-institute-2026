import argparse
import torch
import torch.nn.functional as F
from torchvision import datasets
import torchvision.transforms.v2 as transforms
import os
import sys
import numpy as np
import time
from torch.utils.data import TensorDataset, DataLoader

#for Pyt Lightning
import lightning as L
from lightning.pytorch.plugins.environments import MPIEnvironment
from lightning.pytorch.callbacks import Timer
# Initialize the timer
timer = Timer()

# 1. Initialize the MPI Environment plugin
mpi_env = MPIEnvironment()
# see below for wrappers

# -----------------------------------
#Parameters for training
# -----------------------------------
num_worker2use = 1     #for parallel reading/prefetching of data
batch_size     = 256    # a global batch size (it gets divide but mpi world size)
max_numtrain   = 1024   #for this exercise, train on limited num of input, to save time
max_numtest    = 100 #unused in Pyt and test on limited num of input
epochs         = 20
lrate          = 0.001

data_path      = './data'
run_distributed=True  #to run with data parallelism

#default values for parallel execution
#world_size     =1
#rank           =0
print('INFO, parameters, batch size:',batch_size,'max to train:',max_numtrain)

# -------------------------------------------------------------
#   Define network class object and its 
#             initialization and forward function
#             (other functions are inherited from torch.nn)
# -------------------------------------------------------------
class Net(L.LightningModule):     #<<<---- this was replaced: (torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        numfilt      =16
        self.conv1   = torch.nn.Conv2d(1, numfilt, 3, 1)
        self.linear1 = torch.nn.Linear(numfilt*12*12,32) #after max pooling it wil lbe 12 x12
        self.linear2 = torch.nn.Linear(32, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 3, 2)
        #print('MYINFO rank:',rank,' fwd, after max, x shape:',x.shape)

        x = torch.flatten(x, 1)
        x = self.linear1(x)
        x = F.relu(x)
        x = self.linear2(x)
        output = F.log_softmax(x, dim=1)  #log softmax for classfcnt or binary?
        return output
    
    # --------------------- these are new for Pytorch lightning
    #Pyt Lightning needs `training_step()`, `train_dataloader()` and `configure_optimizers()` to be 
    def training_step(model, batch, batch_idx):
        #optimizer.zero_grad()   #reset optimizer state  PyT Lightning does this
        data, target = batch     #<<-- instead of getting it from trainloader

        output = model(data)                  #get predictions
        loss = F.nll_loss(output, target)     #get loss
        # loss.backward()                       #backprop loss  PyT Lightning does this
        #self.log('train loss:',loss)
        print('MYINFO, rank:',rank, ' train loss:',loss.item())
        return loss 
    def validation_step(model, batch, batch_idx):
        data, target = batch
        #data, target = data.to(device), target.to(device)
        output       = model(data)
        loss         = F.nll_loss(output, target) 
        #self.log('val loss:',loss)
        print('MYINFO, rank:', rank,' val loss:',loss.item())
        return 
    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer

    def on_train_start(self):  #a hook to print info
        print(f"INFO, Rank Check, Global Rank: {self.global_rank} / Process Running.")
        print(f"INFO, Device running the step: {self.device}") 
    # ------------------------ End of new functions

# ---------------------------------------
# this train function to run the epochs loop is replaced
# ---------------------------------------
#def train(model, device, train_loader, optimizer, epoch):

# -------------------------------------------------------------
# Replaced by validation step
# -------------------------------------------------------------
#def test(model, device, test_loader):

# -------------------------------------------------------------
#  Main
# -------------------------------------------------------------
def main(numnodes_2use, numdevices_2use):
    print('INFO, main, starting')
    use_cuda = torch.cuda.is_available() 
    if use_cuda:
        num_gpu = torch.cuda.device_count()
        print('INFO, main, cuda, num gpu:',num_gpu)
        accel_2use="gpu"
    else:
        num_gpu = 0
        print('INFO, main, cuda not available')
        accel_2use="cpu"
    torch.manual_seed(777)
    global rank
    global world_size

    # -------------------------------------------
    #Set up rank info, for print outs and getting local batch size
    # -------------------------------------------
    if 1: # run_distributed: 
       #PyT Lightning use its own mpi environment functions, this is not necessary
       #  but I left it in for print statements to use
       if os.getenv('MASTER_ADDR') is None:
                    os.environ['MASTER_ADDR'] = 'localhost'                    
       if os.getenv('MASTER_PORT') is None:
                    os.environ['MASTER_PORT'] = '12355'
       print('INFO, master addr:',os.environ['MASTER_ADDR'])
       world_size = int(os.environ['OMPI_COMM_WORLD_SIZE'])
       rank       = int(os.environ['OMPI_COMM_WORLD_RANK'])
       local_rank = int(os.environ['OMPI_COMM_WORLD_LOCAL_RANK'])

       print('INFO rank:',rank,' dist setup, rank:',rank, ' world:',world_size, 'locrnk:',local_rank)
       
    # -------------------------------------------
    #prepare images for network as they are loaded
    # -------------------------------------------
    transform=transforms.Compose([
        transforms.ToTensor()]) 

    #We'll load data into arrays directly
    X_train=np.load("./X_train5k.npy")
    Y_train=np.load("./Y_train5k.npy")
    X_test =np.load("./X_test.npy")[0:max_numtest,] #limit size to save time, maybe
    Y_test=np.load("./Y_test.npy")[0:max_numtest,]

    #Scale 0 to 1  - or should we not scale
    X_train = X_train/255.0
    X_test  = X_test/255.0

    X_train = X_train[:,np.newaxis,:, :]
    X_test  = X_test[:,np.newaxis,:, :]
    print('INFO, train,test data loaded') 

    #convert to pytorch tensor, then make it a dataset, so that data loader can work with it
    X_train_tensor        = torch.from_numpy(X_train).float() 
    Y_train_tensor        = torch.from_numpy(Y_train).long()  
    X_test_tensor         = torch.from_numpy(X_test).float() 
    Y_test_tensor         = torch.from_numpy(Y_test).long() 
    # Combine input and target tensors into a TensorDataset object
    my_train_dataset = TensorDataset(X_train_tensor, Y_train_tensor) 
    my_test_dataset  = TensorDataset(X_test_tensor, Y_test_tensor)
    print('train,test tensor datasets set up',  'Xtrain size:',X_train_tensor.size())

    # -------------------------------------------
    #Set up data loaders, a distributed data model needs distributed sampler function
    # -------------------------------------------
    if 1:  #assume it always run_distributed 
        #PyT Lightning adds the samplign
        #train_sampler = torch.utils.data.distributed.DistributedSampler(my_train_dataset)
        #test_sampler = None #no sampler means all tasks run same data
                       #torch.utils.data.distributed.DistributedSampler(my_test_dataset)
        batch_size_worker=int(batch_size/world_size)
        print('INFO, changing loader batch size to:',batch_size,'/',world_size,'=',batch_size_worker)
    else:
        train_sampler = None
        test_sampler  = None
        batch_size_worker = batch_size

    train_loader =torch.utils.data.DataLoader(my_train_dataset, 
            batch_size =batch_size_worker, 
            num_workers=num_worker2use)  #, pin_memory=True, drop_last=True)
                              #removed: sampler   =train_sampler,
    val_loader = torch.utils.data.DataLoader(my_test_dataset, 
            batch_size =batch_size,     
            num_workers=num_worker2use)  #, pin_memory=True, drop_last=True)
                             #removed: sampler   =train_sampler,

    # -------------------------------------------
    #  Set up model and do training loop
    # -------------------------------------------
    model = Net()  #PyT Lightn does the  .to(device)

    #For Pyt Lightning - replace training loop with below code
    #for epoch in range(epochs):
    #    train(model, device, train_loader, optimizer, epoch)
    #    test(model, device, test_loader)
    #  .....

    print('INFO, rank:',rank, ' Setting Up Pytorch Wrapper ')
    trainer = L.Trainer(
      accelerator= accel_2use,
      max_epochs=epochs,
      devices   =numdevices_2use, #<<<<<<<<<------ match this to number of tasks per node 
      num_nodes =numdevices_2use, #<<<<<<<<------- match this to num nodes
      strategy  ="ddp",
      plugins=[mpi_env],
      log_every_n_steps=5,
      callbacks=[timer]    # some timing info
     )
    trainer.fit(model, train_loader, val_loader)  # datamodule)
    print('INFO, rank:', rank , ' Done Running Pytorch Wrapper ')
  
    train_time = timer.time_elapsed("train")
    #val_time = timer.time_elapsed("validate")
    print(f"INFO, Total training time: {train_time} seconds")

if __name__ == '__main__':
    import sys
    numnodes_2use   =int(sys.argv[1])
    numdevices_2use =int(sys.argv[2])  
    print('INFO,args:',numnodes_2use,numdevices_2use)
    main(numnodes_2use, numdevices_2use)


