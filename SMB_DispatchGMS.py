# coding: GB2312
#SMUP-Parallel, SuperMap Universal Processor Parallel.
# Author: WangErQi@supermap.com, SuperMap GIS Institute.
# Desc:
#	���л�ִ��Global Mapper��GMS�ű���
#	��������ת����������Ⱦ�����η������ض����ܡ�
#	�����ڴ�ͳ����Ĳ��л�֧�ֵĸ����Ч�ܿ���������
#license: all user and usage, if include above information.

import sys
import string
import re
import os
import subprocess
from datetime import datetime, date, time

import logging
from tornado.ioloop import IOLoop
from stormed import Connection, Message
import simplejson as json

import SMUP
import SMUP_Image
import SMB_Dispatch

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

#ֱ�����д������	
def runGMS(gmsPathFile):
	strGMPath = r"H:\GlobalMapper11\global_mapper11.exe"
	strGMSCMD = strGMPath + " " + gmsPathFile
	print "��������: ",strGMSCMD
	subprocess.call(strGMSCMD)

def buildJob(f):
	strJob = ["job","do job"]
	strJob[1] = f
	strJob = json.dumps(strJob)	
	msgJob = Message(strJob)
	return msgJob

#�ύ�����������д������	
def dispatchJobs(ch):
	fileTemplate = r".\\Template\T_Shader.gms"	
	strDataPath = r"H:\SRTM\SRTM_GMG_ALL"
	strRenderName = r"GeoRender01"
	
	strOutputFilePath = MakeDir(r"H:\SRTM",strRenderName)	
	strGMSPath = MakeDir(strOutputFilePath,"GMS")
	strLogPath = MakeDir(strOutputFilePath,"log")

	flist = SMUP_Image.scanPathAll(strDataPath)
	for f in flist:
		print ""
		print datetime.now(), "�����ļ�: ",f
		strFilePathName = f
		str_GMSPathFile = buildGMS(fileTemplate,strFilePathName,
			strGMSPath,strLogPath,strRenderName,strOutputFilePath)
		job = buildJob(str_GMSPathFile)
		SMB_Dispatch.send_job(job)
		print "�Ѿ��ύ: ",job
		
def MakeDir(strBaseDir,strNewDir):
	strDir = os.path.join(strBaseDir,strNewDir)
	os.mkdir(strDir)
	return strDir
	
#===============================================================
#TODO:
#1���Զ���������Ŀ¼��gms��log������ʱĿ¼�������ֹ������������=>�����
#2������һ�����ύ�����ȫ������Ⱦ��������
#3������GMS���ļ��ŵ���̨ȥ�����ȱ���Ϊ��ʱ�ļ������С�
#4������udb�����̣�������һ���������С�
#5��ֱ����������������ύ������
#	�磺spawn("start SMB_XGMS.py")������CPU�������Worker���̡�
#===============================================================
if __name__ == '__main__':	
	SMB_Dispatch.handle_Dispatcher = dispatchJobs
	SMB_Dispatch.Start()
	