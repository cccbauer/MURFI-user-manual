# Example real-time Network Based Project

This example will create the necesary folders and scripts on the MURFI platform in order to synchronize and send real-time Network Based information to the 
rt-Psychopy Project to set up a neurofeedback experiment

## Prerequisite 

please make sure you have installed and tested all these before continuing:

[MURFI setup](https://github.com/cccbauer/MURFI-user-manual/blob/main/murfi-setup.md)

[FSL setup](https://github.com/cccbauer/MURFI-user-manual/blob/main/fsl-setup.md)

[rt-PsychoPy setup](https://github.com/cccbauer/MURFI-user-manual/blob/main/rt-PsychoPy/README.md)

## Initialization

On your Ubuntu laptop where MURFI is installed (preferably with rt@rt as the rootname) folow these steps:

`cd /home/rt/`

Fetch this git repo

`git clone https://github.com/cccbauer/MURFI-user-manual.git`

Move the rt-murfi-PyProject to your home directory

`mv MURFI-user-manual/murfi-rt-PyProject/ .`

`cd murfi-rt-PyProject/scripts/`

Ready, no we are able to setu up all necesary files to sart a test run:

##1) Setup a subject folder folder with all relevant information to run the neurofeedback, this needs to happen for each new subject you will run:

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

under `xml` you will find the script that MUEFI will use to extract the neurofeedback information and send it to the rt-PsychoPy script.

under `xfm` you will receive/find the `session_ref.nii` images that will be used to map the ROI masks form where feedback will be computed to the current session images and Fields of View (FOV)
more info on this here

##2) Setup al needed connectins to the Scanner and Stimmulus computer:

From the `/home/rt/murfi-rt-PyProject/scripts` folder we continue to prepare MURFI

`source feedback.sh sub-test setup`

this will show a message like:

 `hello`
`setup`
`subject ID:sub-test`
`/home/rt/murfi-rt-PyProject/subjects/`
`++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++`
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

If there is any issue with the ethernet connections you will see a note stating you need to revise the connections:


`make sure Wi-Fi is off
make sure you are Wired Connected to rt-fMR
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++`


##3) If everything is succesfull we are ready to start the Scan or Simmulation by acquiring our 2vol for registration of ROI masks:

`source feedback.sh sub-test 2vol`

This will pop up MURFI interface ready to receive images from the Scanner like this:


![alt text](https://github.com/cccbauer/MURFI-user-manual/blob/main/png/2vol.png?raw=true)


##4) Now you are ready to recieve images from the Scanner/Simmulator

If you are doing a real scann, the 2vol sequence on the Scanner can be started

If you are doing a simmulation:

open a new terminal:

`cd /home/rt/murfi-rt-PyProject/scripts`

Start the simmulator MURFI singularity image with the flag to just send 2 images:

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

And on the MURFI interface you will see how the images are being received:`

![alt text](https://github.com/cccbauer/MURFI-user-manual/blob/main/png/2vol_recived.png?raw=true)































