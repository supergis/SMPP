"""
向指定的数据集追加影像数据集 
参数:


[in]

string

strDataSourceSrc 源数据源名称; 



[in]

string

strDatasetSrc 源数据集名称; 



[in]

string

strDataSourceDst 被追加数据源别名; 



[in]

string

strDatasetDst 被追加数据集名称; 

返回:成功返回true; 注意:向已存在数据集中追加影像数据集. 
"""

# coding: GB2312
#===================================
#向指定的数据集追加数据集
#AppendDatasetRaster    
#===================================
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
strDatasetSrc="DatasetSrc"
strDatasetDst="DatasetDst"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#打开oracle数据源
if bOpen == 1:
    bAppend=SuperMap.AppendDatasetRaster(odsAlias,strDatasetSrc,odsAlias,strDatasetDst)#追加数据集
    if bAppend == 1:
        print "追加数据集成功"
    else:
        print "追加失败！"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "打开数据源失败！"
    
SuperMap.Exit()#清空组件环境释放内存
