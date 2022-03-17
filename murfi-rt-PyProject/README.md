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

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
created all directories for sub-test
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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






















