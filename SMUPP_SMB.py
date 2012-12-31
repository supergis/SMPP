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
超图地理信息并行处理支持系统总线.
	Based SuperMap Universal Processor-SMUP.
		By SuperMap GIS Institute,2012.
"""
# tuple of all parallel python servers to connect with
ppservers = ()
#ppservers = ("127.0.0.1:60000", )
jobs = []

#def Start(ncpus):
global job_server

#print "CPUs : ", job_server.get_ncpus(),
ncpus = 2
if ncpus > 1:
	job_server = pp.Server(ncpus, ppservers=ppservers)
else:
	job_server = pp.Server(ppservers=ppservers)
print "Starting SMPP with", ncpus, "workers"

def run(flist,Task_Func, Task_params):
	for f in flist:
		print "Commit Task ",f
		jobs.append(job_server.submit(Task_Func, (f,), 
			(), ("math", "string","re","os","time","SMB","SMUP","SMUP_Image")))

def result():
	for job in jobs:
		print "Job Running Result: ", job()

def stat():
	job_server.print_stats()
