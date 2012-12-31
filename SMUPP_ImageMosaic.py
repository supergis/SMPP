# coding: GB2312
#!/usr/bin/env python
#SMUP-Parallel,SuperMap Universal Processor Parallel
# File: SMUP_test.py
# Author: WangEQ, SuperMap GIS Institute.
# Desc: 

import sys
import string
import re
import os
import time
import pp
import SMUP
import SMUP_Image

def buildParamid():
	SMUP_Image.BuildPyramid("I:\\ETM\\UDB\\SRTM_GeoShaderBK_TIF",
		"SRTM_GeoShaderBK_TIF","SRTM_GeoShaderBK_TIF")
	
def imageMosaic(data_path,udbpath,dtName):
	flist = SMUP_Image.scanPath("tif",data_path)
	print "文件总数: ", len(flist)

	#显示影像文件的拼合后全幅信息
	print "Entire Image Dataset Info:", SMUP_Image.calcDatasetInfo(SMUP_Image.getType("tif"),flist)
	SMUP_Image.Tif2UDB_Mosaic(SMUP_Image.getType("tif"),flist,udbpath,dtName)
	#SMUP.SMUP_Close()

#====Main Call===========================
ppservers = ()
job_server = pp.Server(ppservers=ppservers)
print "Starting pp with", job_server.get_ncpus(), "workers"

jobs = []

jobs.append(job_server.submit(imageMosaic, ("D:\SRTM\SRTM_GeoRender01_TIF",
		"I:\\ETM\\UDB\\","SRTM_GeoRender01_TIF"),
		(), ("math", "string","re","os","time","SMUP","SMUP_Image")))
jobs.append(job_server.submit(imageMosaic, ("D:\SRTM\SRTM_GeoShader01_TIF",
		"I:\\ETM\\UDB\\","SRTM_GeoShader01_TIF"),
		(), ("math", "string","re","os","time","SMUP","SMUP_Image")))

jobs.append(job_server.submit(imageMosaic, ("D:\SRTM\SRTM_GeoRenderBK_TIF",
		"I:\\ETM\\UDB\\","SRTM_GeoRenderBK_TIF"),
		(), ("math", "string","re","os","time","SMUP","SMUP_Image")))
#jobs.append(job_server.submit(imageMosaic, ("D:\SRTM\SRTM_GeoShaderBK_TIF",
#		"I:\\ETM\\UDB\\","SRTM_GeoShaderBK_TIF"),
#		(), ("math", "string","re","os","time","SMUP","SMUP_Image")))		

jobs.append(job_server.submit(imageMosaic, ("D:\SRTM\SRTM_GlobalRender_TIF",
		"I:\\ETM\\UDB\\","SRTM_GlobalRender_TIF"),
		(), ("math", "string","re","os","time","SMUP","SMUP_Image")))
jobs.append(job_server.submit(imageMosaic, ("D:\SRTM\SRTM_GlobalShader_TIF",
		"I:\\ETM\\UDB\\","SRTM_GlobalShader_TIF"),
		(), ("math", "string","re","os","time","SMUP","SMUP_Image")))			

for job in jobs:
    	print "Job Running Result: ", job()

print "BuildMosaic Finish."
