# Session 1.2: Getting Started with Expanse

<img src='https://www.sdsc.edu/_files/images/news_items/PR20250505_magnetism_expanse.jpg' width='100%' height='100%'/>

Everything you need to know about getting your account setup to use [Expanse](https://www.sdsc.edu/systems/expanse/index.html) next weeek at the CIML26 Summer Institute.

- Presented by: [Marty Kandes](https://www.sdsc.edu/research/experts/kandes-marty.html)  (mkandes@sdsc.edu)
- Date:  Tuesday, June 16, 2026 (CIML26 Prep Day)

## Prerequisites
- [Session 0: Preparing for the CIML Summer Institute](https://github.com/ciml-org/ciml-summer-institute-2026/tree/main/0_preparation)

## Presentation Slides
- N/A

## Hands-On Exercises

- [Exercise 1: Login via the Expanse User Portal](exercises/login-via-portal.md)
- [Exercise 2: Login via SSH](exercises/login-via-ssh.md)
- [Exercise 3: Check your default SHELL](exercises/check-default-shell.md)
- [Exercise 4: Check your allocation access](exercises/check-alloc-access.md)
- [Exercise 5: Clone the GitHub repository](exercises/clone-github-repo.md)


### Exercise 6: Reconfigure your SHELL environment

Navigate to the Session 1.2. material in the repo on Expanse. 

*Output*
```
[mkandes@login01 ~]$ cd ciml-summer-institute-2026/
[mkandes@login01 ciml-summer-institute-2026]$ cd 1.2_accounts_login_environment_expanse_portal/
[mkandes@login01 1.2_accounts_login_environment_expanse_portal]$ ls
backup-your-bash-env.sh  README.md                remove-ciml26-bash-env.sh
load-ciml26-bash-env.sh  reload-your-bash-env.sh
[mkandes@login01 1.2_accounts_login_environment_expanse_portal]$
```

*Command*
```
chmod +x backup-your-bash-env.sh
```

*Output*
```
[mkandes@login01 1.2_accounts_login_environment_expanse_portal]$ chmod +x backup-your-bash-env.sh
[mkandes@login01 1.2_accounts_login_environment_expanse_portal]$ ls
backup-your-bash-env.sh  load-ciml26-bash-env.sh  README.md  reload-your-bash-env.sh  remove-ciml26-bash-env.sh
[mkandes@login01 1.2_accounts_login_environment_expanse_portal]$
```

*Command*
```
./backup-your-bash-env.sh
```

*Command*
```
chmod +x load-ciml26-bash-env.sh
```

*Output*
```
[mkandes@login01 1.2_accounts_login_environment_expanse_portal]$ ./load-ciml26-bash-env.sh 
.bashrc: OK
.bash_profile: OK
[mkandes@login01 1.2_accounts_login_environment_expanse_portal]$
```

Now log out then back in ...

*Output*
```
[mkandes@login01 1.2_accounts_login_environment_expanse_portal]$ exit
logout
Connection to login.expanse.sdsc.edu closed.
mkandes@hardtack:~$ ssh mkandes@login.expanse.sdsc.edu
(mkandes@login.expanse.sdsc.edu) TOTP code for mkandes: 291893
(mkandes@login.expanse.sdsc.edu) TOTP code for mkandes: 294893
Welcome to Bright release         9.0

                                                         Based on Rocky Linux 8
                                                                    ID: #000002

--------------------------------------------------------------------------------

                                 WELCOME TO
                  _______  __ ____  ___    _   _______ ______
                 / ____/ |/ // __ \/   |  / | / / ___// ____/
                / __/  |   // /_/ / /| | /  |/ /\__ \/ __/
               / /___ /   |/ ____/ ___ |/ /|  /___/ / /___
              /_____//_/|_/_/   /_/  |_/_/ |_//____/_____/

--------------------------------------------------------------------------------

Use the following commands to adjust your environment:

'module avail'            - show available modules
'module add <module>'     - adds a module to your environment for this session
'module initadd <module>' - configure module to be loaded at every login

-------------------------------------------------------------------------------
Last login: Tue Jun 16 09:44:54 2026 from 216.15.51.171
[mkandes@login01 ~]$
```

Once logged back in, check if you have the new environment available.

*Command*
```
echo $CIML26_DATA_DIR
```

*Output*
```
[mkandes@login01 ~]$ echo $CIML26_DATA_DIR
/cm/shared/examples/sdsc/ciml/2026
[mkandes@login01 ~]$
```

### Exercise 7: Create a symlink in your HOME directory to CIML26_DATA_DIR

*Command*
```
ln -s $CIML26_DATA_DIR ciml26-data-dir
```

*Output*
```
[mkandes@login01 ~]$ ln -s $CIML26_DATA_DIR ciml26-data-dir
[mkandes@login01 ~]$ ls 
ciml26-data-dir  ciml-summer-institute-2026  data  projects  scratch  scripts  software
[mkandes@login01 ~]$ ls -lahtr ciml26-data-dir/
total 14G
-rw-r--r--  1 mkandes use300 931M Jun 22  2023 gene_info.gz
-rw-r--r--  1 mkandes use300 209M Jun 26  2023 BookReviews_1M.txt
-rw-r--r--  1 mkandes use300  77M Jun 26  2023 BookReviews_1M.txt.zip
-rw-r--r--  1 mkandes use300 1.1G Jun 26  2023 BookReviews_5M.txt
-rw-r--r--  1 mkandes use300 388M Jun 26  2023 BookReviews_5M.txt.zip
drwxr-xr-x  5 mkandes use300    3 Jun 26  2023 catsVsDogs
-rw-r--r--  1 mkandes use300  62M Jun 26  2023 catsVsDogs.zip
-rw-r--r--  1 mkandes use300 104K Jun 26  2023 daily_weather.xlsx
-rw-r--r--  1 mkandes use300 123M Jun 26  2023 minute_weather.csv
-rw-r--r--  1 mkandes use300  26M Jun 26  2023 minute_weather.csv.zip
-rw-r--r--  1 mkandes use300 298K Jun 26  2023 winequality-white.xlsx
drwxr-xr-x 14 mkandes use300   14 Jun 26  2023 gene_info.parquet
-rw-r--r--  1 mkandes use300 140M Jun 14  2024 cuda-samples-v12.2.zip
-rw-r--r--  1 mkandes use300 138M Jun 14  2024 cuda-samples-v12.2.tar.gz
drwxr-xr-x  6 mkandes use300   12 Jun 14  2024 cuda-samples
-rw-r--r--  1 mkandes use300  165 Jun 23  2025 .llm.yaml
-rw-r--r--  1 mkandes use300  318 Jun 23  2025 .py-light.yml
-rw-r--r--  1 mkandes use300  209 Jun 23  2025 .pytorch-lightning.yaml
-rw-r--r--  1 mkandes use300  334 Aug  4  2025 .ptl.yaml
drwxr-xr-x  5 mkandes use300    3 Aug  4  2025 .galyleo
drwxr-xr-x  3 mkandes use300    1 Jun  4 18:18 ..
-rw-r--r--  1 mkandes use300 4.5G Jun  4 18:19 ptl-cuda-12-1.sif
-rw-r--r--  1 mkandes use300 4.8G Jun  4 18:19 ollama-latest-expanse.sif
-rw-r--r--  1 mkandes use300  123 Jun 15 10:12 conda-pyspark-4.1.2.yaml
drwxr-xr-x  6 mkandes use300   24 Jun 15 18:06 .
-rw-r--r--  1 mkandes use300 1.6G Jun 15 18:07 spark-latest.sif
[mkandes@login01 ~]$
```

### Exercise 8: Test your new command aliases

*Command*
```
srun-compute
```

*Output*
```
[mkandes@login01 ~]$ srun-compute 
[mkandes@exp-6-05 ~]$ squeue --me
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          50937645   compute     bash  mkandes  R       0:08      1 exp-6-05
[mkandes@exp-6-05 ~]$
```

*Command*
```
srun-nairr-gpu-shared
```

*Output*
```
[mkandes@login01 ~]$ srun-nairr-gpu-shared 
srun: Requested partition configuration not available now
srun: job 50938039 queued and waiting for resources
```

*Output*
```
[mkandes@login01 ~]$ squeue --me
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          50938039 nairr-gpu     bash  mkandes PD       0:00      1 (Job's QOS not permitted to use this partition (nairr-gpu-shared allows nairr-gpu-shared-normal not nairr-gpu-shared-eot))
[mkandes@login01 ~]$
```

*Command*
```
jupyter-shared-spark
```

*Output*
```
[mkandes@login01 ~]$ jupyter-shared-spark
ERROR :: Command-line option --qos=normal-eot not recognized or not supported.
ERROR :: galyleo_launch command failed.
[mkandes@login01 ~]$ jupyter-compute-pytorch
ERROR :: Command-line option --qos=normal-eot not recognized or not supported.
ERROR :: galyleo_launch command failed.
[mkandes@login01 ~]$
```

### Exercise 9: Update your copy of the CIML26 GitHub repository

*Command*
```
git pull
```

*Output*
```
[mkandes@login01 ciml-summer-institute-2026]$ git pull
remote: Enumerating objects: 43, done.
remote: Counting objects: 100% (43/43), done.
remote: Compressing objects: 100% (40/40), done.
remote: Total 40 (delta 29), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (40/40), 13.19 KiB | 5.00 KiB/s, done.
From https://github.com/ciml-org/ciml-summer-institute-2026
   288a42d..b58b2c4  main       -> origin/main
Updating 288a42d..b58b2c4
Fast-forward
 1.2_accounts_login_environment_expanse_portal/README.md | 190 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
 1 file changed, 189 insertions(+), 1 deletion(-)
[mkandes@login01 ciml-summer-institute-2026]$
```

## Additional References
- N/A

## About CIML

The [Cyberinfrastructure-Enabled Machine Learning (CIML)](https://ciml.sdsc.edu) CyberTraining program at the [San Diego Supercomputer Center (SDSC)](https://www.sdsc.edu/) teaches researchers and students best practices for effectively running artificial intelligence (AI), machine learning (ML), and deep learning (DL) applications on advanced cyberinfrastructure (CI) and high-performance computing (HPC) systems. 

## Acknowledgements

This material is based upon work supported by the [U.S. National Science Foundation](https://www.nsf.gov) under Award Numbers [CISE/OAC-1928224](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=1928224) and [CISE/OAC-2320934](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2017767). Any opinions,
findings, conclusions, or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the NSF.

<img src='https://nsf.widen.net/content/josuwjrmy6/png/NSF_Official_logo_Med_Res_600ppi.png' alt='NSF Logo' width='250'/>
