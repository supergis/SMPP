# coding: GB2312
#!/usr/bin/env python
#SMUP-Parallel,SuperMap Universal Processor Parallel
# File: SMUPP.py
# Author: WangEQ, SuperMap GIS Institute.
# Desc: 

import math
import sys
import pp
import SMUP
import SMUP_Image

print """
SuperMap Parallel Processor-SMPP. V0.1
超图地理信息并行处理支持系统.
	Based SuperMap Universal Processor-SMUP.
		By SuperMap GIS Institute,2012.
"""
# tuple of all parallel python servers to connect with
ppservers = ()
#ppservers = ("127.0.0.1:60000", )
jobs = []

#def Start(ncpus):
global job_server

ncpus = 1
if ncpus > 1:
	job_server = pp.Server(ncpus, ppservers=ppservers)
else:
	job_server = pp.Server(ppservers=ppservers)
print "Starting SMPP with", job_server.get_ncpus(), "workers"

def run(flist,Task_Func, Task_params):
	for f in flist:
		print "Commit Task ",f
		jobs.append(job_server.submit(Task_Func, (f,), 
			(), ("math", "string","re","os","time","SMUP","SMUP_Image")))

def result():
	for job in jobs:
		print "Job Running Result: ", job()

def stat():
	job_server.print_stats()
