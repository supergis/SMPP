# coding: GB2312
#===================================
#向指定的数据集追加数据集
#AppendDatasetRaster    
#===================================

"""
创建影像数据集 
参数:


[in]

string

strAlias 数据源别名; 



[in]

string

strName 数据集名称; 



[in]

string

strType 数据集类型,取值为: ?Image
 ?DEM
 ?Grid 



[in]

string

strEncType 编码类型,取值为: ?encNONE
 ?encDCT
 ?encSGL
 ?encLZW
 ?encCompound 



[in]

string

strPixfmt 像素类型; ?IPF_MONO
 ?IPF_FBIT
 ?IPF_BYTE
 ?IPF_TBYTE
 ?IPF_RGB
 ?IPF_RGBA
 ?IPF_TRGB （48位真彩色）
 ?IPF_LONGLONG
 ?IPF_LONG
 ?IPF_FLOAT
 ?IPF_DOUBLE 



[in]

int

iWidth 影像宽; 



[in]

int

iHeight 影像高; 



[in]

double

dLeft 地理范围left; 



[in]

double

dTop 地理范围top; 



[in]

double

dRight 地理范围right; 



[in]

double

dBottom 地理范围bottom; 



[in]

int

iBlkSize 影像分块大小,取值为: ?64
 ?128
 ?256
 ?512
 ?1024
 ?2048
 ?4096
 ?8192 

返回:成功返回true. 通过获取影像文件的地理范围创建影像数据集示例: 
"""

import os
import sys
sys.path.append(r"D:\DotNetPythonBin\Bin") #将.net组件的路径添加到环境变量
import smu as SuperMap #导入SuperMap模块

SuperMap.Init()#初始化Python组件环境;

#====================================
#需要修改的参数，以Oracle数据源为例
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

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#打开oracle数据源
if bOpen == 1:
    bCreate=SuperMap.CreateDatasetRaster(odsAlias,dtName,strType,strEncType,strPixfmt,
                                        iWidth,iHeight,dLeft,dTop,dRight,dBottom,iBlkSize)
    if bCreate == 1:
        print "创建栅格数据集成功"
    else:
        print "创建栅格数据集失败"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "打开数据源失败！"
    
SuperMap.Exit()#清空组件环境释放内存

	