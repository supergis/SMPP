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

import SMUP
import SMUP_Image

def listFile(data_path):
	print "Scan Path ",data_path,
	flist = SMUP_Image.scanPath("tif",data_path)
	print "文件总数: ", len(flist)
	return flist
	
def imageMosaic():
	strSourcePath = "H:\SRTM\GeoShader01"
	strOutputPath = "H:\SRTM\UDB"
	strOutputFileName = "SRTM_GeoShader01"
	print "Mosaic: ", strSourcePath
	print "Output: ", strOutputPath,strOutputFileName
	SMUP_Image.Tif2UDB_Mosaic(SMUP_Image.getType("tif"),
		listFile(strSourcePath),	strOutputPath, strOutputFileName,False)
		
def image2UDB():
	SMUP_Image.Tif2UDB(listFile("H:\ETM\TIF"),"I:\\ETM\\UDB\\")

#单独创建影像金塔
def buildParamid():
	SMUP_Image.BuildPyramid("I:\\ETM\\UDB\\SRTM_GeoShaderBK_TIF",
		"SRTM_GeoShaderBK_TIF","SRTM_GeoShaderBK_TIF")

#====Main Call===========================
imageMosaic()
#image2UDB()
#buildParamid()
SMUP.SMUP_Close()
