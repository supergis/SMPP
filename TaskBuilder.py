# coding: GB2312
#Build Task from Template.

import sys
import string
import re
import os
import subprocess
from datetime import datetime, date, time

import SMUP_Image

def buildGMS(fileTemplate,strFilePathName,strGMSPath,strLogPath,
	strRenderName,strOutputFilePath):
	print '�ű�ģ��: ',fileTemplate

	#��ȡģ���ļ�	
	strGMS = ""
	f_Template = open(fileTemplate,"r")
	for line in f_Template:
		strGMS = strGMS + line
	f_Template.close()
	
	print "�����ļ�: ",strFilePathName
	str_dataFile = strFilePathName	
	filepath = os.path.split(strFilePathName)
	
	lists = filepath[1].split('.')
	filename = lists[0] + ".Tif"
	str_outputFile = os.path.join(strOutputFilePath,filename)
	print '����ļ�: ',str_outputFile
	
	str_logFile = os.path.join(strLogPath,filename + '.log')
	
	#�滻�ű���Ŀ���ļ����
	strGMS=strGMS % {"logFile":str_logFile,
		"dataFile":str_dataFile,
		"renderName":strRenderName,
		"outputFile":str_outputFile
		}
	
	#���������ļ�
	str_GMSPathFile = os.path.join(strGMSPath,filename + '.gms')
	print '�����ļ�: ', str_GMSPathFile
	
	#�����������
	f_GMS= open(str_GMSPathFile,"w")
	f_GMS.write(strGMS)
	f_GMS.close()
	return str_GMSPathFile
	
def runGMS(gmsPathFile):
	strGMPath = r"H:\GlobalMapper11\global_mapper11.exe"
	strGMSCMD = strGMPath + " " + gmsPathFile
	print "��������: ",strGMSCMD
	#os.system(strGMSCMD)
	subprocess.call(strGMSCMD)

#===============================================================
if __name__ == '__main__':
	fileTemplate = r".\\Template\T_Render.gms"
	strGMSPath = r"H:\SRTM\GeoShader01\GMS"
	strLogPath = r"H:\SRTM\GeoShader01\log"
	strRenderName = r"GeoShader01"
	strOutputFilePath = r"H:\SRTM\GeoShader01"

	flist = SMUP_Image.scanPathAll(r"H:\SRTM\SRTM_GMG_ALL")
	for f in flist:
		print ""
		print datetime.now(), "�����ļ�: ",f
		strFilePathName = f
		str_GMSPathFile = buildGMS(fileTemplate,strFilePathName,strGMSPath,strLogPath,
			strRenderName,strOutputFilePath)
		runGMS(str_GMSPathFile)
	
	