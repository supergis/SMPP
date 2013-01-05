"""
获取影像文件地理范围 
参数:


[in]

string

strType 文件类型; ?fileTIF
 ?fileIMG
 ?fileBMP
 ?fileJPG
 ?fileGRD
 ?fileRAW
 ?fileUSGSGRID
 ?fileSIT
 ?fileArcinfoGrid
 ?fileIDR 



[in]

string

strFilePath 文件全路径名; 

返回:返回4X2的数组,前4个元素为影像的地理范围,后2个元素为影像宽/高.
"""
# coding: GB2312

import sys
sys.path.append(r'D:\DotNetPythonBin\Bin')
import string
import re
import smu as SuperMap
import os
import time
SuperMap.Init()


#=====================================
#需要修改的参数  
testPath=r"F:\2012\python范例程序\Data\GetImageGeoRef\海港.tif"
fileType = "fileTIF"
#需要修改的参数
#=====================================

L=[]

                        
#获取每个影像文件的左右地理范围，保存到数组
L= SuperMap.GetImageGeoRef(fileType,testPath)
print L
#获取影像信息，左右上下边界值以及宽高
left=float(L[0][0])
top=float(L[0][1])
right=float(L[0][2])
bottom=float(L[0][3])
width=int(L[1][0])
height=int(L[1][1])
#打印影像左右上下宽高值
print "左："+str(left)+"  上:"+str(top)+"  右"+str(right)+"  下"+ str(bottom)
print "宽："+ str(width)+" 高："+str(height)

SuperMap.Exit()#清空环境，释放内存
