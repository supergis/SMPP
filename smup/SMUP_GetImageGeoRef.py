"""
��ȡӰ���ļ�����Χ 
����:


[in]

string

strType �ļ�����; ?fileTIF
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

strFilePath �ļ�ȫ·����; 

����:����4X2������,ǰ4��Ԫ��ΪӰ��ĵ���Χ,��2��Ԫ��ΪӰ���/��.
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
#��Ҫ�޸ĵĲ���  
testPath=r"F:\2012\python��������\Data\GetImageGeoRef\����.tif"
fileType = "fileTIF"
#��Ҫ�޸ĵĲ���
#=====================================

L=[]

                        
#��ȡÿ��Ӱ���ļ������ҵ���Χ�����浽����
L= SuperMap.GetImageGeoRef(fileType,testPath)
print L
#��ȡӰ����Ϣ���������±߽�ֵ�Լ����
left=float(L[0][0])
top=float(L[0][1])
right=float(L[0][2])
bottom=float(L[0][3])
width=int(L[1][0])
height=int(L[1][1])
#��ӡӰ���������¿��ֵ
print "��"+str(left)+"  ��:"+str(top)+"  ��"+str(right)+"  ��"+ str(bottom)
print "��"+ str(width)+" �ߣ�"+str(height)

SuperMap.Exit()#��ջ������ͷ��ڴ�
