# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster    
#===================================

"""
����Ӱ�����ݼ� 
����:


[in]

string

strAlias ����Դ����; 



[in]

string

strName ���ݼ�����; 



[in]

string

strType ���ݼ�����,ȡֵΪ: ?Image
 ?DEM
 ?Grid 



[in]

string

strEncType ��������,ȡֵΪ: ?encNONE
 ?encDCT
 ?encSGL
 ?encLZW
 ?encCompound 



[in]

string

strPixfmt ��������; ?IPF_MONO
 ?IPF_FBIT
 ?IPF_BYTE
 ?IPF_TBYTE
 ?IPF_RGB
 ?IPF_RGBA
 ?IPF_TRGB ��48λ���ɫ��
 ?IPF_LONGLONG
 ?IPF_LONG
 ?IPF_FLOAT
 ?IPF_DOUBLE 



[in]

int

iWidth Ӱ���; 



[in]

int

iHeight Ӱ���; 



[in]

double

dLeft ����Χleft; 



[in]

double

dTop ����Χtop; 



[in]

double

dRight ����Χright; 



[in]

double

dBottom ����Χbottom; 



[in]

int

iBlkSize Ӱ��ֿ��С,ȡֵΪ: ?64
 ?128
 ?256
 ?512
 ?1024
 ?2048
 ?4096
 ?8192 

����:�ɹ�����true. ͨ����ȡӰ���ļ��ĵ���Χ����Ӱ�����ݼ�ʾ��: 
"""

import os
import sys
sys.path.append(r"D:\DotNetPythonBin\Bin") #��.net�����·����ӵ���������
import smu as SuperMap #����SuperMapģ��

SuperMap.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ�������Oracle����ԴΪ��
server="sfc60" 
user="testMTT"
pwd="testMTT"
odsAlias="oracle"
dtName="CreateDatasetRasterTest"
strType="Image" 
strEncType = "encDCT"
strPixfmt = "IPF_RGB"
iWidth=50
iHeight=50
dLeft = 0
dTop =50
dRight =50
dBottom =0
iBlkSize = 256
bMultiBands = 0
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#��oracle����Դ
if bOpen == 1:
    bCreate=SuperMap.CreateDatasetRaster(odsAlias,dtName,strType,strEncType,strPixfmt,
                                        iWidth,iHeight,dLeft,dTop,dRight,dBottom,iBlkSize)
    if bCreate == 1:
        print "����դ�����ݼ��ɹ�"
    else:
        print "����դ�����ݼ�ʧ��"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "������Դʧ�ܣ�"
    
SuperMap.Exit()#�����������ͷ��ڴ�

	