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

def SMUP_test():
	print "SUMP_test Start."
	SMUP.SMUP_Version()

def test_smu():
    #SMUP.SMUP_Init()
    SMUP.SMUP_Close()

def test_image_PixelFormat(flist):
    for f in flist:
          print SMUP_Image.getPixelFormatOne(SMUP_Image.getType("tif"),f),'\r\n'

def test_image_Info(flist):
    for f in flist:
          print SMUP_Image.calcDatasetInfoOne(SMUP_Image.getType("tif"),f),'\r\n'
        
def test_image_FileName(flist):
    for f in flist:
          print SMUP_Image.getFileName(f),'\r\n'

      
def test_image():
    data_path = "H:\ETM\TIF2"
    flist = SMUP_Image.scanPath("tif",data_path)
    print flist.count
    #SMUP_Image.list2File("I:\ETM\FileList.txt",flist)
    test_image_PixelFormat(flist)
    #test_image_FileName(flist)
    
    #显示所有影像文件信息
    #test_image_Info(flist)
    
    #显示影像文件的拼合后全幅信息
    #print "Entire Image Dataset Info:",SMUP_Image.calcDatasetInfo(SMUP_Image.getType("tif"),flist)

    #SMUP_Image.Tif2UDB(flist,r"I:\\ETM\\UDB\\")
    
test_image()

#test_smu()	
