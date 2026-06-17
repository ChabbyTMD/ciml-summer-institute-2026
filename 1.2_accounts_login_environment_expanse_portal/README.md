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
- [Exercise 6: Reconfigure your SHELL environment (TO BE UPDATED SOON)](exercises/reconfig-shell-env.md)
- [Exercise 7: Create a symlink](exercises/create-symlink.md)

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
