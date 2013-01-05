"""
只创建金字塔层 
参数:
[in]string strDsAlias 数据源别名; 
[in]string strDtName 数据集名称; 

返回:成功返回true. 
注意:
为新创建的影像数据集创建金字塔; 
只创建金字塔层，并不计算金字塔层数据. 
此方法优点在于,创建大范围影像数据集,并向其追加数据场景;可大大节约时间. 
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
dtName="UGCIMAGE_TF_NoValue"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#打开oracle数据源
if bOpen == 1:
    bBuild=SuperMap.BuildPyramidTiersOnly(odsAlias,dtName)#创建影像金字塔
    if bBuild == 1:
        print "创建金字塔成功"
    else:
        print "创建影像金字塔失败！"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "打开数据源失败！"

SuperMap.Exit()#清空组件环境释放内存
