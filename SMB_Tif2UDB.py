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

#=================================================================
def do_job(job):
	print "Job ToUDB:", job
	SMB.sendStatus("Job Begin: %r"%job)
	SMUP_Image.Tif2UDBOne(job,"H:\SRTM\UDB",False)
	SMB.sendStatus("Job Finish: %r"%job)
	
if __name__ == '__main__':
	SMB.handle_Processor = do_job	
	SMB.Start()
