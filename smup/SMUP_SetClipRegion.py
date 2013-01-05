"""
为影像数据集设置裁剪多边形 
参数:


[in]

string

strDataSourceRst 影像数据集所在数据源名称; 



[in]

string

strDatasetRst 影像数据集名称; 



[in]

string

strDataSourceVct 裁剪多边形所在数据源名称; 



[in]

string

strDatasetVector 裁剪多边形所在数据集名称; 



[in]

int

smId 裁剪多边形smid; 

注意:裁剪多边形在指定的矢量数据集中.
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
dtName="SetClipRegion"
dtRName="SetClipRegion_R"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#打开oracle数据源
if bOpen == 1:
    bSetClipRegion=SuperMap.SetClipRegion(odsAlias,dtName,odsAlias,dtRName,1)#为影像数据集设置裁剪多边形
    if SetClipRegion == 1:
        print "为影像数据集设置裁剪多边形成功"
    else:
        print "为影像数据集设置裁剪多边形失败！"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "打开数据源失败！"

SuperMap.Exit()#清空组件环境释放内存
