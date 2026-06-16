# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# Define common allocation and job-related environment variables
declare -xr CIML26_ACCOUNT='sds280'
declare -xr CIML26_RES_CPU='ciml26cpu'
declare -xr CIML26_RES_GPU='ciml26gpu'
declare -xr CIML26_QOS_CPU='normal-eot'
declare -xr CIML26_QOS_GPU='nairr-gpu-shared-eot'

# Define pre-staged container and data directories
declare -xr CIML26_DATA_DIR='/cm/shared/examples/sdsc/ciml/2026'

# Define srun-based interactive session command aliases
alias srun-shared="srun --account=${CIML26_ACCOUNT} --reservation=${CIML26_RES_CPU} --partition=shared --nodes=1 --ntasks-per-node=1 --cpus-per-task=4 --mem=16G --time=04:00:00 --pty --wait=0 /bin/bash"
alias srun-compute="srun --account=${CIML26_ACCOUNT} --reservation=${CIML26_RES_CPU} --partition=compute --qos=${CIML26_QOS_CPU} --nodes=1 --ntasks-per-node=1 --cpus-per-task=128 --mem=242G --time=04:00:00 --pty --wait=0 /bin/bash"
alias srun-nairr-gpu-shared="srun --account=${CIML26_ACCOUNT} --reservation=${CIML26_RES_GPU} --partition=nairr-gpu-shared --qos=${CIML26_QOS_GPU} --nodes=1 --ntasks-per-node=1 --cpus-per-task=10 --mem=92G --gpus=1 --time=04:00:00 --pty --wait=0 /bin/bash"

# Prepend the GALYLEO_INSTALL_DIR to each user's PATH
export PATH="/cm/shared/apps/sdsc/galyleo:${PATH}"

# Define galyleo-based Jupyter notebook session command aliases
alias jupyter-shared-spark="galyleo launch --account ${CIML26_ACCOUNT} --reservation ${CIML26_RES_CPU} --partition shared --cpus 4 --memory 64 --time-limit 04:00:00 --env-modules singularitypro --sif ${CIML26_DATA_DIR}/spark-latest.sif --bind /expanse,/scratch,/cm --quiet"
alias jupyter-nairr-gpu-shared-pytorch="galyleo launch --account ${CIML26_ACCOUNT} --partition nairr-gpu-shared --qos ${CIML26_QOS_GPU} --cpus 4 --memory 92 --gpus 1 --time-limit 04:00:00  --env-modules singularitypro --sif ${CIML_DATA_DIR}/ptl-cuda-12-1.sif --bind /expanse,/scratch,/cm --nv --quiet"
alias jupyter-compute-pytorch="galyleo launch --account ${CIML26_ACCOUNT} --partition compute --cpus 128 --memory 242 --time-limit 04:00:00  --env-modules singularitypro --sif ${CIML_DATA_DIR}/ptl-cuda-12-1.sif --bind /expanse,/scratch,/cm --quiet"
alias jupyter-nairr-gpu-shared-llm="galyleo launch --account ${CIML26_ACCOUNT} --reservation ${CIML26_RES_GPU} --partition nairr-gpu-shared --qos ${CIML26_QOS_GPU} --cpus 8 --memory 96 --gpus 1 --time-limit 04:00:00 --sif ${CIML_DATA_DIR}/ollama-latest-expanse.sif --nv --bind /expanse,/scratch,/cm --quiet"
