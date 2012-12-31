# coding: GB2312
#!/usr/bin/env python
#SMUP-Parallel,SuperMap Universal Processor Parallel
# File: SMUPP.py
# Author: WangEQ, SuperMap GIS Institute.
# Desc: 

import math
import time
import sys
import SMUP
import SMUP_Image
import SMB
import subprocess

#=================================================================
def do_gms(job):
	print "Job ToUDB:", job
	SMB.sendStatus("Job Begin: %r"%job)
	runGMS(job)
	SMB.sendStatus("Job Finish: %r"%job)

def runGMS(gmsPathFile):
	strGMPath = r"H:\GlobalMapper11\global_mapper11.exe"
	strGMSCMD = strGMPath + " " + gmsPathFile
	print "运行任务: ",strGMSCMD
	subprocess.call(strGMSCMD)
	
if __name__ == '__main__':
	SMB.handle_Processor = do_gms
	SMB.Start()
