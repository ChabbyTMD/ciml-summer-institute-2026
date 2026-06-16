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

### Exercise 1: Log into Expanse via Open OnDemand

We'll get started by logging into Expanse via the web-based Expanse User Portal at [https://portal.expanse.sdsc.edu](https://portal.expanse.sdsc.edu).

You'll first be prompted to choose your organization. Choose **ACCESS-CI** as your organizzation, not your home institution. Then input your ACCESS-CI username and password.

Upon a successful login, you should be presented with the Expanse User Portal dashboard.

Click on the Expanse Shell Access app to get a web-based interactive login shell. 

### Exercise 2: Log into Expanse via SSH

Next we'll test your direct SSH access to Expanse. Use your preferred SSH client to login.

*Command*
```
ssh mkandes@login.expanse.sdsc.edu
```


*Output*
```
mkandes@hardtack:~$ ssh mkandes@login.expanse.sdsc.edu
(mkandes@login.expanse.sdsc.edu) TOTP code for mkandes: 201505
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
Last login: Tue Jun 16 09:37:51 2026 from 132.249.233.139
[mkandes@login01 ~]$
```

If you cannot login, try to register (again) for 2FA. See the Expanse User Guide.

### Exercise 3: Check your default SHELL on Expanse

Once logged into Expanse either via the User Portal or SSH, please check your default SHELL.

*Command*
```
echo $SHELL
```

*Output*
```
[mkandes@login01 ~]$ echo $SHELL
/bin/bash
[mkandes@login01 ~]$
```

Do you have a BASH shell?

### Exercise 4: Check your allocations on Expanse

Next, let's verify you are listed on the CIML26 allocation (**sds280**) for next week.

*Command*
```
expanse-client user -p
```

*Output*
```
```

If you are not listed on the allocation, please let us know.

### Exercise 5: Clone the CIML26 GitHub repository to your HOME directory

Next, please clone this GitHub repository to your HOME directory on Expanse.

*Command*
```
git clone https://github.com/ciml-org/ciml-summer-institute-2026.git
```

*Output*
```
```

### Exercise 6: Reconfigure your SHELL environment

### Exercise 7: Create a symlink in your HOME directory to CIML26_DATA_DIR

*Command*
```
ln -s /path/to/original /path/to/link
```

*Output*
```
```

### Exercise 8: Test your new command aliases

### Exercise 9: Update your copy of the CIML26 GitHub repository

## Additional References
- N/A

## About CIML

The [Cyberinfrastructure-Enabled Machine Learning (CIML)](https://ciml.sdsc.edu) CyberTraining program at the [San Diego Supercomputer Center (SDSC)](https://www.sdsc.edu/) teaches researchers and students best practices for effectively running artificial intelligence (AI), machine learning (ML), and deep learning (DL) applications on advanced cyberinfrastructure (CI) and high-performance computing (HPC) systems. 

## Acknowledgements

This material is based upon work supported by the [U.S. National Science Foundation](https://www.nsf.gov) under Award Numbers [CISE/OAC-1928224](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=1928224) and [CISE/OAC-2320934](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2017767). Any opinions,
findings, conclusions, or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the NSF.

<img src='https://nsf.widen.net/content/josuwjrmy6/png/NSF_Official_logo_Med_Res_600ppi.png' alt='NSF Logo' width='250'/>
