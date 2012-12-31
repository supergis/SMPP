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

print """Usage: python sum_primes.py [ncpus]
    [ncpus] - the number of workers to run in parallel,
    if omitted it will be set to the number of processors in the system"""

# tuple of all parallel python servers to connect with
ppservers = ()
#ppservers = ("127.0.0.1:60000", )

if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    job_server = pp.Server(ncpus, ppservers=ppservers)
else:
    job_server = pp.Server(ppservers=ppservers)
print "Starting pp with", job_server.get_ncpus(), "workers"

#=================================================================
#scan path,prepare TaskList.
data_path = "H:\ETM\TIF2"
#data_path = "I:\ETM\TIF"
flist = SMUP_Image.scanPath("tif",data_path)
print "Scan Path ",data_path,"Finish."    

def Task_Call(f):
	print "Task_Call For: ",f
	#print SMUP_Image.getPixelFormatOne(SMUP_Image.getType("tif"),f),'\r\n'
	SMUP_Image.Tif2UDBOne(f,"I:\\ETM\\UDB\\")
	return True

def Task_Func(f):
	call = Task_Call(f)
	return call 

jobs = []
for f in flist:
	print "Commit Task ",f
	jobs.append(job_server.submit(Task_Func, (f, ), (Task_Call, ), 
		("math", "string","re","os","time","SMUP","SMUP_Image")))

#for job in jobs:
  #  	print "Job Running Result: ", job()

job_server.print_stats()

