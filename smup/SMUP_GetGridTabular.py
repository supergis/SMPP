"""
获取栅格属性表,保存为指定名称的属性数据集. 
参数:
[in]string strDsAlias 数据源别名; 
[in]string strGridName 结果数据集名称; 
[in]string strTabName 结果数据集名称; 

返回:成功返回true. 
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
dtName="SetNoValue"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#打开oracle数据源
if bOpen == 1:
    bBuild=SuperMap.SetNoValue(odsAlias,dtName,0)#设置无值
    if bBuild == 1:
        print "设置无值成功"
    else:
        print "设置无值失败"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "打开数据源失败！"

SuperMap.Exit()#清空组件环境释放内存
