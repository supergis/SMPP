# coding: GB2312
#SMUP-Parallel, SuperMap Universal Processor Parallel.
# Author: WangErQi@supermap.com, SuperMap GIS Institute.
# Desc:
#	并行化执行Global Mapper的GMS脚本。
#	适用数据转换、地形渲染、地形分析等特定功能。
#	适用于传统软件的并行化支持的改造和效能快速提升。
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
	print '脚本模板: ',fileTemplate

	#读取模板文件	
	strGMS = ""
	f_Template = open(fileTemplate,"r")
	for line in f_Template:
		strGMS = strGMS + line
	f_Template.close()
	
	print "输入文件: ",strFilePathName
	str_dataFile = strFilePathName	
	filepath = os.path.split(strFilePathName)
	
	lists = filepath[1].split('.')
	filename = lists[0] + ".Tif"
	str_outputFile = os.path.join(strOutputFilePath,filename)
	print '输出文件: ',str_outputFile
	
	str_logFile = os.path.join(strLogPath,filename + '.log')
	
	#替换脚本中目标文件序号
	strGMS=strGMS % {"logFile":str_logFile,
		"dataFile":str_dataFile,
		"renderName":strRenderName,
		"outputFile":str_outputFile
		}
	
	#生成任务文件
	str_GMSPathFile = os.path.join(strGMSPath,filename + '.gms')
	print '任务文件: ', str_GMSPathFile
	
	#生成任务参数
	f_GMS= open(str_GMSPathFile,"w")
	f_GMS.write(strGMS)
	f_GMS.close()
	return str_GMSPathFile

#直接运行处理进程	
def runGMS(gmsPathFile):
	strGMPath = r"H:\GlobalMapper11\global_mapper11.exe"
	strGMSCMD = strGMPath + " " + gmsPathFile
	print "运行任务: ",strGMSCMD
	subprocess.call(strGMSCMD)

def buildJob(f):
	strJob = ["job","do job"]
	strJob[1] = f
	strJob = json.dumps(strJob)	
	msgJob = Message(strJob)
	return msgJob

#提交到调度器运行处理进程	
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
		print datetime.now(), "处理文件: ",f
		strFilePathName = f
		str_GMSPathFile = buildGMS(fileTemplate,strFilePathName,
			strGMSPath,strLogPath,strRenderName,strOutputFilePath)
		job = buildJob(str_GMSPathFile)
		SMB_Dispatch.send_job(job)
		print "已经提交: ",job
		
def MakeDir(strBaseDir,strNewDir):
	strDir = os.path.join(strBaseDir,strNewDir)
	os.mkdir(strDir)
	return strDir
	
#===============================================================
#TODO:
#1、自动创建附属目录（gms、log）和临时目录，减少手工并输入参数。=>已完成
#2、可以一次性提交多个（全部）渲染处理任务。
#3、保存GMS到文件放到后台去做，先保存为临时文件再运行。
#4、整合udb入库过程，到其中一个进程运行。
#5、直接启动多进程运行提交的任务。
#	如：spawn("start SMB_XGMS.py")，根据CPU启动多个Worker进程。
#===============================================================
if __name__ == '__main__':	
	SMB_Dispatch.handle_Dispatcher = dispatchJobs
	SMB_Dispatch.Start()
	