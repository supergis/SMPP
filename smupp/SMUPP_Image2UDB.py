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
import SMUPP

#=================================================================
#scan path,prepare TaskList.
def listFile(data_path):
	print "Scan Path ",data_path,
	flist = SMUP_Image.scanPath("tif",data_path)
	print "�ļ�����: ", len(flist)
	return flist
	
#�����������ʹ��.
#���ոú�����д��������ִ�к���.
def 	Task_Func(f):
	print "Run Task",f
	
def	Task_Tif2UDB(f):
	print "Task Tif2UDB: ",f
	SMUP_Image.Tif2UDBOne(f,"H:\SRTM\UDB",False)
	#SMUP_Image.Tif2UDBOne(f,"I:\\ETM\\UDB\\",False)
	return True

flist = listFile("H:\SRTM\TIF")
#SMUPP.run(flist,Task_Func,"")
SMUPP.run(flist,Task_Tif2UDB,"")
SMUPP.result()
SMUPP.stat()



