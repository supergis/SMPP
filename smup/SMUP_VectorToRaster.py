# coding: GB2312
#===================================
#向指定的数据集追加数据集
#AppendDatasetRaster    
#===================================

"""
矢量转栅格 
参数:
[in]string strDataSourceSrc 源数据源名称; 
[in]string strDtVector 待转换的矢量数据集名称; 
[in]string strDataSourceDst 结果数据源名称: 
[in]string strDtRaster 结果栅格数据集名称: 
[in]string strFieldName 栅格值字段名称: 
[in]int iPixelFormat 结果栅格像素格式, 取值为: 
 ?8 IPF_BYTE
 ?16 IPF_TBYTE
 ?24 IPF_RGB
 ?32 IPF_RGBA
 ?320 IPF_LONG
 ?3200 IPF_FLOAT
 ?6400 IPF_DOUBLE 

[in]double dResolution 结果栅格分辨率,设置为0时,使用内部默认计算值: 

返回:成功返回true. 

"""

import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #将.net组件的路径添加到环境变量
import smu as SuperMap #导入SuperMap模块

SuperMap.Init()#初始化Python组件环境;

#====================================
#需要修改的参数
server=r"F:\Temp\2012-08-25\rvconversion.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开oracle数据源
if bOpen == 1:
            dtRaster = 'DQ35_Raster'
            SuperMap.DeleteDataset(odsAlias, dtRaster)
            SuperMap.VectorToRaster(odsAlias, 'DQ36', odsAlias, dtRaster, 'SmUserID', 320, 933)
            SuperMap.CloseDataSource(odsAlias)  
else:
    print "打开数据源失败！"
    
SuperMap.Exit()#清空组件环境释放内存
