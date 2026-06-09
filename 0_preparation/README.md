# Preparing for the CIML Summer Institute

**SESSION:** 0_preparation

## Instructions
You will get the most out of the CIML Summer Institute if you are prepared prior to the event. By brushing up on your knowledge of Linux and installing all necessary software on your laptop before the event, you’ll be able to focus your attention on the skills and topics that are most relevant to machine learning.

This section contains a set of detailed start-up instructions, beginning with setting up your account and connecting to Expanse, to configuring your laptop for running visualization software. Please read the documents and exercises carefully, and complete all necessary steps before the event. Feel free to ask questions or if you have any problems with the start-up tasks

<a name="top">Contents
* [Expanse Account Access](#accounts)
* [Expanse User Guide](#expanse-guide)
* [Large Language Model (LLM) Account](#llm-account)
* [Basic Skills](#basic-skills)
* [Computer Requirements](#comp-req)
* [Github, Slack and Zoom](#Github-Slack-Zoom)
  * [Github](#github)
  * [Slack](#slack)
  * [Zoom](#zoom)

##  Expanse Account Access: <a name="accounts"></a>
NOTE: **ACCESS ID profile must be up-to-date with the following:**
 * U.S. Institutional Email and U.S. Institution (must match)
 * Country of Residence

Note: If not, you will not be able to access the system.

Your ACCESS-CI account has been added to our training allocation. We do not use local passwords.  For access to Expanse you will need to login with your ACCESS-CI credentials. If you have forgotten your ACCESS-CI portal password you can reset it at https://identity.access-ci.org/password-reset // [Reset ACCESS-CI Password](https://identity.access-ci.org/password-reset).

In addition, for direct access via ssh,  if you have not already done so, you will need to set up 2FA at SDSC.  (This 2FA is independent of the 2FA you enrolled in with your ACCESS-CI portal account). To enroll please visit https://passive.sdsc.edu // [Enroll with SDSC's 2FA](https://passive.sdsc.edu)

Be sure to choose the **“Globus”** option to login and use ACCESS CI as the organization **(not your home institution)** when you login. Once you are logged in on the page there should be a “Manage 2FA” button. If you click that you should get the option to read a QR code from your authenticator app to link into your account. **_(NOTE:  This change may take up to 15 minutes to update on the system)._**

Full instructions can be found at: https://www.sdsc.edu/systems/expanse/user_guide.html#narrow-wysiwyg-2 // [Visit for full istructions](https://www.sdsc.edu/systems/expanse/user_guide.html#narrow-wysiwyg-2)
You can go to: https://passive.sdsc.edu

### Account access may be used:
 * Via SSH directly to login.expanse.sdsc.edu // [Direct login to SSH](login.expanse.sdsc.edu )
 * Via the Expanse Portal: https://portal.expanse.sdsc.edu // [Login via Expanse Portal](https://portal.expanse.sdsc.edu)

**For questions related to your Expanse account, please contact consult@sdsc.edu.** In your email subject line, enter "Expanse Access: CIML 2026."

[Back to Top](#top)
<hr>

## Expanse User Guide <a name="expanse-guide"></a>
Please read the Expanse user guide and familiarize yourself with the hardware, file systems, batch job submission, compilers and modules. The guide can be found here:
 * [Expanse User Guide](https://www.sdsc.edu/support/user_guides/expanse.html)
 * [Expanse Landing Page](https://expanse.sdsc.edu/)

Note: if you have any difficulties getting set up, please contact Institute staff at consult@sdsc.edu.

  [Back to Top](#top)
<hr>
  
##  Large Language Model Account: <a name="llm-account"></a>
There will be a [Hugging Face](https://huggingface.co/) demo on day 3, if you would like to follow along, you can sign-up for a free [Hugging Face account](https://huggingface.co/join), unless you already have an account. This is completely optional. 

[Back to Top](#top)
<hr>
  
## Basic Skills <a name="basic-skills"></a>
There are several basic skills needed in order to access and run jobs on HPC systems. These include training webinars and hands-on materials:
 * [Interactive Videos](https://education.sdsc.edu/training/interactive/) // https://education.sdsc.edu/training/interactive/
 * [COMPLECS training](https://github.com/orgs/sdsc-complecs/repositories) // https://github.com/orgs/sdsc-complecs/repositories

We also have a collection of mini-tutorials that you can access:
 * [Basic HPC Linux Skills](https://github.com/sdsc-hpc-training-org/basic_skills) // https://github.com/sdsc-hpc-training-org/basic_skills
 * [HPC Security](https://github.com/sdsc-hpc-training-org/hpc-security) // https://github.com/sdsc-hpc-training-org/hpc-security
 * [Connecting to Expanse](https://github.com/sdsc-hpc-training-org/hpc-security/blob/master/connecting-to-hpc-systems/connect-to-expanse.md) // https://github.com/sdsc-hpc-training-org/hpc-security/blob/master/connecting-to-hpc-systems/connect-to-expanse.md
 * [Basic_Linux_Skills on Expanse](https://github.com/sdsc-hpc-training-org/basic_skills/tree/master/basic_linux_skills_expanse) // https://github.com/sdsc-hpc-training-org/basic_skills/tree/master/basic_linux_skills_expanse
 * Using Interactive Compute Nodes on [Expanse](https://github.com/sdsc-hpc-training-org/basic_skills/tree/master/interactive_computing)
 * How to Run Notebooks on Expanse: We use a secure notebook launching tool called Galyleo:
 * [Tutorial](https://github.com/sdsc/galyleo) // https://github.com/sdsc/galyleo
 * Video on [Running Jupyter Notebooks on Expanse](https://education.sdsc.edu/training/interactive/?id=series-1&from=202206_cimlsi)


[Back to Top](#top)
<hr>

 ##  Computer Requirements <a name="comp-req"></a>
 * You will need to bring your own laptop for the summer institute. This will be used both for running software locally and connecting to SDSC’s supercomputers.
 * Wireless network will be available throughout the SDSC building using either UCSD-Guest or eduroam
   ** [Learn more about using wifi as a Guest at UC San Diego](https://blink.ucsd.edu/technology/network/connections/wireless/guest.html)
 * Remember your charger. There will be extension cords throughout the room for charging devices


[Back to Top](#top)
<hr>
 
 ##  GitHub, Slack, and Zoom  <a name="Github-Slack-Zoom"></a>
 
### Github: <a name="github"></a>
* Training material will be located on the CIML Summer Institute [GitHub repo](https://github.com/ciml-org/ciml-summer-institute-2026).
  * Presentation slides for each session will be posted as soon as they become available. 
* One of the hands-on sessions will require a GitHub account.
  * If you do not already have one, you can [create a free personal GitHub account here](https://docs.github.com/en/github/getting-started-with-github/signing-up-for-github/signing-up-for-a-new-github-account). 
  * Learn more about [basic GitHub usage on SDSC systems](https://github.com/sdsc-hpc-training-org/basic_skills/tree/master/using_github)

### Slack:  <a name="slack"></a>
* We will also be using Slack as our main platform for announcements, where participants can communicate and ask for help. Download ([Windows](https://slack.com/downloads/windows), [MacOS](https://slack.com/downloads/mac), or [Linux](https://slack.com/downloads/linux)) and [get started](https://slack.com/help/articles/218080037-Getting-started-for-new-Slack-users). and get started. Zoom chat will be disabled during the preparation day. Make sure to turn on your Slack notifications to receive alerts.
See **"Preparation Information | CIML Summer Institute 2026"** email received for the link to join the Slack workspace for this institute.            

### Zoom:  <a name="zoom"></a>
* We will be using Zoom for preparation day on Tuesday, June 16, 2026, from 9am - 11am (Pacific Time).
* You will need to install the latest [Zoom](https://zoom.us/download) client, which is available for Windows, MacOS and Linux. Once installed, you can test your microphone and camera interface with Zoom [here](https://zoom.us/test). You can find more information on Zoom system requirements, including bandwidth requirements [here](https://support.zoom.us/hc/en-us/articles/201362023-System-Requirements-for-PC-Mac-and-Linux).  

Connection details were sent as a calendar invite to all CIML participants. You should have received an invite for the preparation day on Tuesday, June 16, 2026, from 9am - 11am (Pacific Time). If you did not receive this an invite, please contact cmw007@ucsd.edu. 

Note: While Prep Day is a virtual event, the main CIML Summer Institute sessions (Tuesday, June 24 - Thursday, June 26) will be held in person and will not be available remotely.

[Back to Top](#top)
<hr>
