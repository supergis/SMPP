# coding: GB2312
#!/usr/bin/env python
#SMUP-Parallel,SuperMap Universal Processor Parallel
# File: SMUPP.py
# Author: WangEQ, SuperMap GIS Institute.
# Desc: 

import math
from datetime import datetime, date, time
import sys
import SMUP
import SMUP_Image
import SMB_Dispatch
import subprocess

#=================================================================
def do_test(job):
	tStart = datetime.now()
	for i in range(0,100000):
		#print "[",datetime.now(),"]", "TEST sendStatus:", i
		SMB_Dispatch.sendStatus("TEST sendStatus: %s"%i)
	tEnd = datetime.now()
	strTestInfo = "TEST Time:%s [%s]--[%s]"%(i,tStart,tEnd)
	print strTestInfo
	SMB_Dispatch.sendStatus(strTestInfo)
	SMB_Dispatch.close()
	
if __name__ == '__main__':
	SMB_Dispatch.handle_Dispatcher = do_test
	SMB_Dispatch.Start()
