# coding: GB2312
#!/usr/bin/env python
#SMUP-Parallel,SuperMap Universal Processor Parallel
# File: SMUPP.py
# Author: WangEQ, SuperMap GIS Institute.
# Desc: 

import math
import time
import sys

import logging
from tornado.ioloop import IOLoop
from stormed import Connection, Message
import simplejson as json

import SMUP
import SMUP_Image
import SMB_Dispatch

#=================================================================
#scan path,prepare TaskList.
def listFile(data_path):
	print "Scan Path ",data_path,
	flist = SMUP_Image.scanPath("tif",data_path)
	print "文件总数: ", len(flist)
	return flist

def buildJob(f):
	strJob = ["job","do job"]
	strJob[1] = f
	strJob = json.dumps(strJob)	
	msgJob = Message(strJob)
	return msgJob
	
def dispatchJobs(ch):
	flist = listFile("H:\ETM\TIF2")
	for f in flist:
		job = buildJob(f)
		print "Dispatch Job:",f
		SMB_Dispatch.send_job(job)
		
if __name__ == '__main__':
	SMB_Dispatch.handle_Dispatcher = dispatchJobs
	SMB_Dispatch.Start()
