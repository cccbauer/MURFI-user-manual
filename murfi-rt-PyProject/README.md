# Example real-time Network Based Project

This example will create the necesary folders and scripts on the MURFI platform in order to synchronize and send real-time Network Based information to the 
rt-Psychopy Project to set up a neurofeedback experiment

## Prerequisites

please make sure you have installed and tested all these before continuing:

[MURFI setup](https://github.com/cccbauer/MURFI-user-manual/blob/main/murfi-setup.md)

[FSL setup](https://github.com/cccbauer/MURFI-user-manual/blob/main/fsl-setup.md)

[rt-PsychoPy setup](https://github.com/cccbauer/MURFI-user-manual/blob/main/rt-PsychoPy/README.md)

[anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)

[nypype](https://nipype.readthedocs.io/en/latest/users/install.html)

## Initialization

On your Ubuntu laptop where MURFI is installed (preferably with rt@rt as the rootname, if not some paths have to change on the scripts) folow these steps:

`cd /home/rt/`

### Fetch this git repo

`git clone https://github.com/cccbauer/MURFI-user-manual.git`

Move the rt-murfi-PyProject to your home directory

`mv MURFI-user-manual/murfi-rt-PyProject/ .`

`cd murfi-rt-PyProject/scripts/`

Ready, no we are able to setu up all necesary files to sart a test run:

### 1) Setup a subject folder folder with all relevant information to run the neurofeedback, this needs to happen for each new subject you will run:

`source createxml.sh sub-test setup`

This will show this message:

`++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++`

`created all directories for sub-test`

`++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++`

This means that all directories for "sub-test" were succesfully created

To check all the subfolders you can open a new terminal and navigate to:

`/home/rt/murfi-rt-PyProject/subjects/sub-test`

and in the created "sub-test" folder you will find :

`fsfs  img  log  mask  rest  ses-localizer  ses-real  ses-sham  xfm  xml`

under `xml` you will find the script that MURFI will use to extract the neurofeedback information and send it to the rt-PsychoPy script.

under `xfm` you will receive/find the `session_ref.nii` images that will be used to register the ROI masks in MINI space to the current session images and Fields of View (FOV)

more info on this [here]

### 2) Setup al needed connectins to the Scanner and Stimmulus computer:

From the `/home/rt/murfi-rt-PyProject/scripts` folder we continue to prepare MURFI

`source feedback.sh sub-test setup`

this will show a message like:

`++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++`\
`+ Wellcome to MURFI real-time Neurofeedback`\
`+ running  setup`\
`+ subject ID: sub-test`\
`+ working dir: /home/rt/murfi-rt-PyProject/subjects/`\
`++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++`\
`checking the presence of scanner and stim computer`
`PING 192.168.2.1 (192.168.2.1) 56(84) bytes of data.`

`64 bytes from(192.168.2.1): icmp_seq=1 ttl=116 time=8.31 ms`
`64 bytes from(192.168.2.1): icmp_seq=2 ttl=116 time=10.4 ms`
`64 bytes from(192.168.2.1): icmp_seq=3 ttl=116 time=10.9 ms`

`--- 192.168.2.1 ping statistics ---`
`3 packets transmitted, 3 received, 0% packet loss, time 2028ms`

`PING 192.168.2.6 (192.168.2.6) 56(84) bytes of data.`


`64 bytes from(192.168.2.6): icmp_seq=1 ttl=116 time=8.31 ms`
`64 bytes from(192.168.2.6): icmp_seq=2 ttl=116 time=10.4 ms`
`64 bytes from(192.168.2.1): icmp_seq=3 ttl=116 time=10.9 ms`
`--- 192.168.2.6 ping statistics ---`

`3 packets transmitted, 3 received, 0% packet loss, time 2028ms`
`++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++`

This sets up all connections to Scanner (192.168.2.1) and Stimmulus computer (192.168.2.6)

If there is any issue with the network connections you will see a note stating you need to revise the connections:


`make sure Wi-Fi is off
make sure you are Wired Connected to rt-fMR
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++`


### 3) Now we are ready to acquire the Resting State scan for Network Extraction.:

From the `/home/rt/murfi-rt-PyProject/scripts` folder we continue to prepare MURFI

`source feedback.sh sub-test ses-localizer run-01 resting_state`

This will pop-up MURFI interface ready to receive 250 Resting State images from the Scanner like this:

![alt text](https://github.com/cccbauer/MURFI-user-manual/blob/main/png/resting.png?raw=true)

Now you can start the Resting State scan on the scanner or alternatively run the Resting State simmulation like this:

Open a new terminal and from

`/home/rt/murfi-rt-PyProject/scripts` 

start the Resting State as follows:

`$ /home/rt/singularity-images/murfi2.sif ./servedata.sh 250vol`

this will start sending images as if it ware a resting state for 250 volumes at 1.2 seconds TR:

`1 using niiStem=img/img`\
`2 using series=1`\
`3 using numImgs=250`\
`4 using firstImg=1`\
`5 using numSlices=68`\
`6 using tr=1200000`\
`7 using port=15000`\
`8 using host=localhost`\
`loading nifti img/img-00001-00001.nii`\
`made connection, loading image`\
`sending img  1`\
`sending info of size 616`\
`sending img of size 2654208`\
`loading nifti img/img-00001-00002.nii`\
`made connection, loading image`\
`sending img  2`\
` etc. . . `\

### 4) Compute personalized Networks for Feedback

Once the Resting State has finished, close the MURFI terminal and start the network extraction pipeline as follows:

`source feedback.sh sub-test ses-localizer run-01 extract_rs_networks`

this will initialize the network extraction peline as follows:

`+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++`\
`compiling resting state run into analysis folder`\
`calculating resting state networks this will take about 25 minutes`\
`+ started at: Thu Jul  7 16:21:44 EDT 2022e`\

and pop-up FSL MELODIC browser window:

![alt text](https://github.com/cccbauer/MURFI-user-manual/blob/main/png/ica.png?raw=true)


### 5) Process Resting State ROI masks for Neurofeedback:

Once the MELODIC ICA Resting State Network computation has finished we are ready to get the ROIs for our neurofeedback paradigm. 

In the current setup we will compute:

a) Default Mode Network (dmn)
b) Central Excecutive Network (cen)
c) Somatomotor Cortex (smc)


`source feedback.sh sub-test ses-localizer run-01 process_roi_masks`

which will display:

`++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++`\
`+ Generating DMN, CEN and SMC masks.`\
`++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++`\

and when finished computing the ROI masks for DMN, CEN and SMC display them for QA in fsleyes:

![alt text](https://github.com/cccbauer/MURFI-user-manual/blob/main/png/fsleyes.png?raw=true)

If everything is succesfull we are ready to start the Neurofeedback Scans

### 3)Acquiring '2vol' for registration of ROI mask to current subject space and field of view

If you ran the resting state network computation and mask creation between scans and are starting a new rea-time Neurofeedback scan or run, repeat setup as described in step (2).

Now we are ready for aquiring the updated field of view

`source feedback.sh sub-test ses-nf1 run-01 2vol`

This will pop-up MURFI interface ready to receive 2 volumes from the Scanner like this:


![alt text](https://github.com/cccbauer/MURFI-user-manual/blob/main/png/2vol.png?raw=true)


### 4) Now you are ready to recieve images from the Scanner/Simmulator

If you are doing a real scann, the **2vol** sequence on the Scanner can be started

If you are doing a simmulation:

open a new terminal:

`cd /home/rt/murfi-rt-PyProject/scripts`

Start the simmulator MURFI singularity image with the **2vol** flag to just send 2 images:

`/home/rt/singularity-images/murfi2.sif ./servedata.sh 2vol`

`1 using niiStem=img/img`

`2 using series=1`
`3 using numImgs=2`
`4 using firstImg=1`
`5 using numSlices=68`
`6 using tr=1200000`
`7 using port=15000`
`8 using host=localhost`
`loading nifti img/img-00001-00001.nii`
`made connection, loading image`
`sending img  1`
`sending info of size 616`
`sending img of size 2654208`
`loading nifti img/img-00001-00002.nii`
`made connection, loading image`
`sending img  2`
`sending info of size 616`
`sending img of size 2654208`
`failed to connect`

And on the MURFI interface you will see how the images are being received:

![alt text](https://github.com/cccbauer/MURFI-user-manual/blob/main/png/2vol_recived.png?raw=true)

CONTROL-C to quit this MURFI interface if it not automatically quit.


### 5)  Register MNI ROIs to the subjects space of current scan

`source feedback.sh sub-test ses-nf1 run-01 register`

This will start the registration of the masks created in stem (found in 

`/home/rt/murfi-rt-PyProject/subjects/sub-test/mask/mni`
`cen_mni.nii.gz  dmn_mni.nii.gz  smc_mni.nii.gz  stg_mni.nii.gz`

and will pop-up fsleyes to check the registration

![alt text](https://github.com/cccbauer/MURFI-user-manual/blob/main/png/fsleyes_subject.png?raw=true)

Now you are ready to start the real-time neurofeecback scans

### 6) Network Based real-time Neurofeedback 

The order of this next step is important:

First: Start the Murfi interface to receive the feedback run:

`source feedback.sh sub-test run-01 dmn`

This will pop-up the interface to receive images similar to the 2vol one seen above with the difference that the lenth is 120 seconds and the regression to compute the beta values on murfi is continuous over the whole run.

![alt text](https://github.com/cccbauer/MURFI-user-manual/blob/main/png/rtdmn.png?raw=true)

On the stimulus computer:

Start PsychoPy
Run `rt-network_feedback.py` script

Read the instructions and go all the way to "waiting for scanner trigger"

if running a real subject, now the scan can begin and the triggers will start the experiment

If running a simulation you would neet to:

Press "t" at the same time than starting the simmulator on the second terminal:

Press "t" on the stimmulus computer

Hit enter after this line on the second termial:

`/home/rt/singularity-images/murfi2.sif ./servedata.sh 120vol`

This will start the feedback scann and you can see how the data is integrated and the feedback display on  the stimulus computer is being updated:

![alt text](https://github.com/cccbauer/MURFI-user-manual/blob/main/png/rtdmn_run.png?raw=true)
