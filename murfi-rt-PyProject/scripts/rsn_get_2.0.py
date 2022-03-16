#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nipype.interfaces import fsl
from nipype.interfaces.fsl import MotionOutliers
#get_ipython().run_line_magic('matplotlib', 'inline')
import os.path
import subprocess
import os
from glob import glob
import sys

# In[2]:



subjID = sys.argv[1]



# # get correls to Yeo 7networks

# In[4]:



correlfile="/home/rt/rtBANDA/data/sub-%s/ses-01/func/sub-%s_ses-01_task-rest_run-01_bold.gica/groupmelodic.ica/Yeo_rsn_correl.txt" %(subjID,subjID)
split_outfile='/home/rt/rtBANDA/data/sub-%s/ses-01/func/sub-%s_ses-01_task-rest_run-01_bold.gica/groupmelodic.ica/melodic_IC_' %(subjID,subjID)
dmn_component='/home/rt/rtBANDA/data/sub-%s/ses-01/func/sub-%s_ses-01_task-rest_run-01_bold.gica/groupmelodic.ica/dmn_mni_uthresh.nii.gz' %(subjID,subjID)
cen_component='/home/rt/rtBANDA/data/sub-%s/ses-01/func/sub-%s_ses-01_task-rest_run-01_bold.gica/groupmelodic.ica/cen_mni_uthresh.nii.gz' %(subjID,subjID)
smc_component='/home/rt/rtBANDA/data/sub-%s/ses-01/func/sub-%s_ses-01_task-rest_run-01_bold.gica/groupmelodic.ica/smc_mni_uthresh.nii.gz' %(subjID,subjID)
# # get DMN, CEN, SMC

# In[6]:


import pandas as pd
from nipype.interfaces.fsl import ImageStats
fslcc_info = pd.read_csv(correlfile, sep=' ', skipinitialspace=True, header=None)
list(fslcc_info)
fslcc_info.sort_values(by=[1, 2], ascending=False, inplace=True)
dmn_info = fslcc_info.loc[fslcc_info[1] == 7, :].values
cen_info = fslcc_info.loc[fslcc_info[1] == 6, :].values
smc_info = fslcc_info.loc[fslcc_info[1] == 2, :].values

roi1 = int(dmn_info[0, 0]-1)
roi2  = int(cen_info[0, 0]-1)
roi3  = int(smc_info[0, 0]-1)

dmnfuncfile=split_outfile+'%0.4d.nii.gz' % roi1
cenfuncfile=split_outfile+'%0.4d.nii.gz' % roi2
smcfuncfile=split_outfile+'%0.4d.nii.gz' % roi3

os.system('cp %s %s' %(dmnfuncfile,dmn_component))
os.system('cp %s %s' %(cenfuncfile,cen_component))
os.system('cp %s %s' %(smcfuncfile,smc_component))




