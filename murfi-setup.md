# MURFI-user-manual

This manual describes the use of MURFI software to deliver real-time functional magnetic resonance imaging neurofeedback 
(rt-fMRI-nf).

MURFI (multivariate and univariate real-time functional imaging) is a software package for real-time processing of functional brain images for neuroscience applications.

rt-fMRI-nf is a type of biofeedback in which real-time online fMRI signals are used to self-regulate brain (neuro) function. Since it's advent in 1995 significant progress has been made in fMRI neurofeedback techniques. Specifically, the use of rt-fMRI-nf has advanced the understanding of causal involvement of modified brain activity in modified behavior. rt-fMRI-nf was developed in 1995 (Cox et al., 1995), and proof-of concept for rt-fMRI-nf as a potential neurotherapeutic tool for the treatment of brain disorders was demonstrated in 2005 (deCharms et al., 2005). There have since been substantial advancements related to rt-fMRI-nf technology and implementation, with reports of rt-fMRI-nf modification of function in several brain structures. Although rt-fMRI-nf has multiple potential applications as a clinical neuroimaging tool, the research to date has been focused on the use of rt-fMRI-nf to alter brain function and behavior.


#The latest version of MURFI can pull fMRI images from the scanner in two ways:

# Vsend option

MURFI can read images from vsend considering the Siemens preheader for this option you need to get Vsend on your Scanner.

# Initiate C2P agreement before running MURFI on Siemens scanners

To obtain the individual functional images in real time a proprietary data transfer sequence needs to be added to the respective sequences. The code can be obtained via a C2P agreement to get the Vsend patch on the fMRI sequences for real-time image sending. 

Please initiate the C2P process as follows:

Go to the [Athinoula A. Martinos Clone C2P](https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.nmr.mgh.harvard.edu%2Flab%2Fwebdev%2Fclone-c2p&data=05%7C01%7Cc.bauer%40northeastern.edu%7Cea729988697f40593f0808db3776e5ae%7Ca8eec281aaa34daeac9b9a398b9215e7%7C0%7C0%7C638164756028903418%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=xwa9Jq9Xq1EDjhU2n%2B9XrbrhvWrYM9%2BTmTbbeNs9NK0%3D&reserved=0) site 

Under "Which C2P are you requesting?" select:

"Real-time transfer"< br / >

and fill out the Requestor Contact Information 

Otherwise please fill out [this form](https://github.com/cccbauer/MURFI-user-manual/blob/main/C2P_Request_template_SiemensMR_updated.docx) and send to Chang, Yulin <yulin.chang@siemens-healthineers.com>


# DICOM option 

Another way to read input images by MURFI is from real-time DICOM export.

For this method you need to add the

**murfi2-bold-dotaddin** 

Please contact [Paul Wighton](https://www.nmr.mgh.harvard.edu/user/8244) at <PWIGHTON@mgh.harvard.edu> to get the dotaddin instrucitons and patch.

# MURFI on other scanners
 
Alternatively, for non-Siemens scanners or for your own Siemens functors, Murfi will accept data over TCP/IP conformant with the following structured information:

https://github.com/gablab/murfi2/blob/master/src/io/RtExternalSenderImageInfo.h


# MURFI System Requirements

We recomend a laptop that has characteristics simmilar to this [Dell](https://www.dell.com/en-us/shop/dell-computer-laptops/alienware-m18-r2-gaming-laptop/spd/alienware-m18-r2-laptop/#customization-anchor)

# Direct TCP/IP communication 

To enable direct TCP/IP communication between the scanner, MURFI software and the presentation Psychopy computer please setup a local network following the diagram below with following IP adresses:

Siemens console: 192.168.2.1 <br/>
MURFI:           192.168.2.5 <br/>
psychopy:        192.168.2.6 <br/>

Netmask for all 255.255.255.240

To install the network you can use the following [switch]([https://system76.com/laptops/gazelle#specs](https://www.amazon.com/NETGEAR-Ethernet-Unmanaged-Lifetime-Protection/dp/B00MPVR50A/ref=sr_1_1?dib=eyJ2IjoiMSJ9.oYrfDmoDQOAa9bOsMN_eFiQ25BbPTyOm8qO36ZX3HT3EG0rPU1I4UwcuFqTAtciFhxP0P52Kam7x9xX8hE8hHIY-hlzbrN0VMovZRzD5hWCE4CWF6sPTASJL3mkU5FvHg3lYpXHUZgQIVm7heeM0x6FxTPoxzQJA_R6QmvDrIWD6OTBvcrWys8MGeCWdamojq-75gStNf_IMyjpIFRqsqO0BQoP-Tko8Flsu-6XFEdkynE8ky9ZAsX6VXYsI5OWsQ0hGMklMsuvaon04WMNiS0Y02SAUtN-D-mOWQR_nCE8.Fg4eyGNwsHibzNptnqfld8I71_A5S3NjYasz1QVr7h0&dib_tag=se&keywords=NETGEAR+ProSAFE+8-Port+Gigabit+Switch+%28GS108%29&qid=1729206042&s=amazon-devices&sr=1-1)) or something similar

When setting it up the network you can place the switch behind the host, unplugge from the Siemens host the ethernet cable coming from MARS/equipment-room (192.168.2.2) and plugg it into the switch. Then get 3 ethernet cables to connect the Siemens host (192.168.2.1), MURFI computer (192.168.2.5), and PsychoPy computer (192.168.2.6) to the switch. Finally, make sure to manually set the IP for the MURFI and PsychoPy computers per diagram below.

 Note, when installing the switch make sure the Siemens host is turned off since it could lock up due to the temporary loss of network connectivity to MARS/equipment-room during the installation process.

 
Finally, we keep the switch installed all the time and have not experienced any issues with the Siemens host being able to communicate effectively with MARS (and vice versa). But if you experience any issues that Siemens needs to debug, you may need to temporarily remove the switch such that the Siemens host and MARS/equipment-room connectivity is direct as it is now (we have not had to do this, but depending on the issue this may be needed).


![alt text](https://github.com/cccbauer/MURFI-user-manual/blob/main/png/localNetwork.png?raw=true)


# Prepare laptop with Ubuntu to run MURFI

Install Ubuntu preferably on a laptop exclusive for delivering rt-fMRI-nf.

This instalation works best on Ubuntu 20.4 but you may also try to Install the latest [long term support (LTS) Ununtu](https://ubuntu.com/download/desktop)

Open a terminal and update all:

`sudo apt-get update`

# Install MURFI

Please refer to [MURFI git repo](https://github.com/gablab/murfi2) for additional installation instructions.

Here we will go step by step:

## Install Git

`sudo apt install git`

## Clone the Murfi Git repository

`git clone https://github.com/gablab/murfi2.git`

## get Singularity

get the latest Singularity and closely follow this [installation guide](https://sylabs.io/guides/3.0/user-guide/installation.html)

## pull and compile the latest MURFI version

`sudo singularity build -F murfi.sif docker://ohinds/murfi:framewise-displacement`

## Downloading a dataset to run the example

Before running murfi, please download the example data and set environment variables.

`cd ~/`


`wget https://dl.dropbox.com/s/1vvrz2g4tbzoh5c/murfi_example_data.tgz &&
tar -xzf murfi_example_data.tgz &&
rm murfi_example_data.tgz`

`export MURFI_SUBJECTS_DIR="$PWD"`
`export MURFI_SUBJECT_NAME=murfi_example_data`

## Running the example using the Singularity container

Next, you can run murfi. `murfi2.sif` is the path to the Singularity container, which is a file. The `murfi` bit after the path to the container is the command that is executed within the container. Everything after `murfi` is arguments that are passed to `murfi`.

`singularity exec singularity-images/murfi2.sif murfi -f murfi_example_data/scripts/neurofeedback.xml`

or

`singularity run singularity-images/murfi2.sif murfi -f murfi_example_data/scripts/neurofeedback.xml`

This will pop up the `murfi` interface.

## Scanner Simmulator

To finalize the example we will simmulate a scanner feeding in the individual volumes.

open a new termial

`cd /home/rt/murfi_example_data/scripts`

Start the Scanner simmulation

`~/singularity-images/murfi2.sif ./servedata.sh`

This should start sending individual volumes to `murfi` which will then show them on the left hand side as axial slices with the region of interest (ROI) from where the feedback will be computed in pink (visual cortex).


## Alternative MURFI on Mac OS or Windows using Vagrant

MURFI can also be used through [Vagrant](https://www.vagrantup.com/) and [Virtual Box](https://www.virtualbox.org/) and follow this  
[Using Vagrant](Using-Vagrant/README.md#Using Vagrant)







## Alternatively first compile docker container

`docker build --tag murfi2 --file Dockerfile ..`

`sudo docker save [DOCKER IMAGE ID] -o murfi_new.tar`

`sudo singularity build murfi_new.sif docker-archive://murfi_new.tar` 

this should yield something along this lines (don't copy):

`Successfully built 83ded15c4a1b`
`Successfully tagged murfi2:latest`

Note: sometimes the docker deamon has to be started manually before buildding the container:

`systemctl start docker`

`sudo apt-get update && sudo apt-get install -y \
    build-essential \
    libssl-dev \
    uuid-dev \
    libgpgme11-dev \
    squashfs-tools \
    libseccomp-dev \
    pkg-config`
    
 ### get Go
 
 Download this Go version [go1.17.5.linux-amd64.tar.gz installer](https://go.dev/doc/install)
 
Extract the archive you downloaded into /usr/local, creating a Go tree in /usr/local/go.

Important: This step will remove a previous installation at /usr/local/go, if any, prior to extracting. Please back up any data before proceeding.

 For example, run the following as root or through sudo:
    
 `cd ~/Downloads`

 `sudo rm -rf /usr/local/go`
 
 `sudo tar -C /usr/local -xzf go1.17.5.linux-amd64.tar.gz`

 Add /usr/local/go/bin to the PATH environment variable.

 You can do this by adding the following line to your $HOME/.profile or /etc/profile (for a system-wide installation):

   `export PATH=$PATH:/usr/local/go/bin`

   Note: Changes made to a profile file may not apply until the next time you log into your computer. To apply the changes immediately, just run the shell commands directly or execute them from the profile using a command such as source $HOME/.profile.
    Verify that you've installed Go by opening a command prompt and typing the following command:

`go version`

   Confirm that the command prints the installed version of Go.

 ## Download Singularity latest repo

Here we used [Singularity- 3.7.2\3](https://github.com/apptainer/singularity/releases/download/v3.7.3/singularity-3.7.3.tar.gz)

`wget -d github.com/apptainer/singularity/releases/download/v3.7.3/singularity-3.7.3.tar.gz`

`tar -xzf singularity-3.7.3.tar.gz`

## Compile singularity

`cd ./singularity`

`./mconfig`

`make -C ./builddir `

`sudo make -C ./builddir install`

`singularity version`

   Confirm that the command prints the installed version of Singularity.
   
## To make a Singularity container of murfi

Lets convert the Docker image to a Singularity container:

`cd ~/murfi2/docker/`

`sudo singularity build murfi2.sif docker-daemon://murfi2:latest`

## move singularity image to appropriate folder:

`mkdir ~/singularity-images/`

`mv murfi2.sif ~/singularity-images/`







