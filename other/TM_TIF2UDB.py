# coding: GB2312

#===================================================
#影像成批导入SuperMap UDB格式工具.
#基本流程:
#1、扫描目录，或者根据经纬度按照块的高宽生成文件列表。
#2、扫描存在的文件，获取最大的坐标范围。
#3、扫描存在的文件，获取像素格式。
#4、遍历文件列表，对于存在的文件追加到打开的数据库UDB中。
#5、创建金字塔索引，以加快显示速度。（可选的过程）
#===================================================

import sys
import string
import re
import os
import time

def getType(ext):
	if ext.lower() == 'tif':
		return 'fileTIF'
	elif ext.lower() == 'img':
		return 'fileIMG'

#根据行列数构建datafiles，用于追加    
def BuildFileListCol(type, path, nCol):
	print ""
	print("----------Build Files List-----------")	
	
	reMatch = '[\d\D]*.tif$'
	if type=='img':
		reMath = '[\d\D]*.img$'
	
	C01=46
	C02=48
	R01=3
	R02=4
	
	#nCol = int(Col)
	print("Col: %(C00)02d" % {"C00": nCol})
	print("Row: %(R01)02d-%(R02)02d" % {"R01":R01,"R02":R02})

	strFileName =""
	strFilePath =""
	FileCount = 0
	for j in range(R01,R02):
		ConvertTif2UDBOnce(path,nCol,j)
		FileCount = FileCount + 1
		print("Files Count: %(FC)02d" % {"FC":FileCount})
	return FileCount

#根据行列数构建datafiles，用于追加
def BuildFileList(type, path):
	print ""
	print("----------Build Files List-----------")	
	datafiles = []
	reMatch = '[\d\D]*.tif$'
	if type=='img':
		reMath = '[\d\D]*.img$'
	
	C01=46
	C02=48
	R01=1
	R02=5	
	print("Col: %(C01)02d-%(C02)02d" % {"C01":C01,"C02":C02})
	print("Row: %(R01)02d-%(R02)02d" % {"R01":R01,"R02":R02})

	strFileName =""
	strFilePath =""
	FileCount = 0
	for i in range(C01,C02):
		for j in range(R01,R02):
			ConvertTif2UDBOnce(path,i,j)
			FileCount = FileCount + 1
			print("Files Count: %(FC)02d" % {"FC":len(FileCount)})
	return datafiles

def calcDatasetInfoOnce(type,file):
	print("----------CalcDatasetInfo-----------")	
	L=[]	
	left=[]
	top=[]
	right=[]
	bottom=[]
	ratiox=[]
	ratioy=[]

	#获取每个影像文件的左右地理范围，保存到数组
	if os.path.exists(file):
		L= smu.GetImageGeoRef(type,file)
		print file
		print "File Extend: ", L

		l=float(L[0][0])
		t=float(L[0][1])
		r=float(L[0][2])
		b=float(L[0][3])
		w=int(L[1][0])
		h=int(L[1][1])
		x=(r-l)/w
		y=(t-b)/h
		
		left.append(l)
		right.append(r)
		top.append(t)
		bottom.append(b)
		ratiox.append(x)
		ratioy.append(y)

		#获取左右上下边界
		dLeft=min(left)
		dRight=max(right)
		dTop=max(top)
		dBottom=min(bottom)
			
		#获取分辨率，影像最小分辨率作为数据集分辨率
		dRatioX = min(ratiox)
		dRatioY = min(ratioy)
		
		#计算影像数据集宽度和高度
		nWidth = int((dRight-dLeft)/dRatioX)
		nHeight = int((dTop-dBottom)/dRatioY)
		
		#重新计算，保证分辨率正确
		dRight=dLeft+dRatioX*nWidth
		dBottom=dTop-dRatioY*nHeight
		L = [nWidth, nHeight, dLeft, dTop, dRight, dBottom]	
	else:
		print("File NoExist:" + file)
		#L = [100, 100, 0, 0, 100, 100]			
	return L

#获取像素格式,找到第一个实际存在的文件.
def GetPixelFormat(fileType, file):
	print("----------GetPixelFormat-----------")	
	pixType = smu.GetImagePixelFormatName(fileType, file)
	return pixType

#删除已存在的输出文件
def ClearFile(dtFile):
	#清理初始环境,需要调整...
	udb = dtFile + '.udb'
	udd = dtFile + '.udd'
	if os.path.exists(udb):
		os.remove(udb)
	if os.path.exists(udd):
		os.remove(udd)
		
#将TIF转为UDB	
def ConvertTif2UDBOnce(path,c,r):
	strFileName="N-%(C)02d-%(R)02d" % {"C":c,"R":r*5}
	strFilePath=os.path.join(path,"N-%(C)02d-%(R)02d.tif" % {"C":c,"R":r*5})	
	OutputPath = "H:\\ETM\\TIF_SM\\"
	
	dtFile = os.path.join(path,strFileName)
	
	print 'Build FileName: ',strFileName,dtFile	
	print "--Convert Block Files: ",strFilePath
	if os.path.exists(strFilePath):
		print "Convert: " + strFilePath
	else:
		print "Not Exist: " + strFilePath
		exit()
	
	L=[]
	L=smu.GetImageGeoRef(getType("TIF"),strFilePath)
	print "File Extend: ", L

	l=float(L[0][0])
	t=float(L[0][1])
	r=float(L[0][2])
	b=float(L[0][3])
	w=int(L[1][0])
	h=int(L[1][1])
		
	pixType = GetPixelFormat(getType("TIF"), strFilePath)
	print "Data Pixel Type: ",pixType	
	
	odsAlias = strFileName
	dtName = odsAlias
	dtName = dtName.replace('-','_')	
	print "Clear UDB File..."
	print dtName
	
	ClearFile(dtFile)
	
	print "Create Datasource..."
	isOpen=smu.OpenDataSource(OutputPath+odsAlias,'','', 'sceUDB', odsAlias)
	
	print "Import Dataset...",strFilePath
	#创建数据集		
	bCreate = smu.CreateDatasetRaster(odsAlias,dtName, 
			'Image', 'encDCT', pixType, w, h , l, t, r , b, 256)
	smu.AppendRasterFile(odsAlias,dtName,getType("tif"), strFilePath)
		
	print "BuildPyramid..."
	#smu.BuildPyramid(odsAlias, dtName)
	smu.CloseDataSource(odsAlias)
	print "==Finished.==========="




#==========================
#主执行函数.
#--------------------------
if __name__=='__main__':
	print len(sys.argv), sys.argv
	
	if len(sys.argv) < 2:
		print "Please Input Column Number."
		exit
	
	ugo="..\\..\\SMU\\"
	sys.path.append(ugo)
	import smu

	nCol = int(sys.argv[1])
	
	#==============================
	print "Begin import to SuperMap UDB..."
	fileType='tif'
	path='H:\ETM\TIF'
	#path = os.path.join(root, path)
	BuildFileListCol(fileType, path, nCol)
	
	#清空环境，释放内存	
	smu.Exit()	
	
