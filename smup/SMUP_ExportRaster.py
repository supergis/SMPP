# coding: GB2312
#===================================

import os
import sys

"""
导出为影像文件 
参数:
[in]string strDsAlias 数据源别名; 
[in]string strName 影像数据集名称; 
[in]string strType 文件类型, 取值为: 
 ?fileTIF
 ?fileIMG
 ?fileBMP
 ?fileJPG
 ?filePNG
 ?fileSIT 
[in]string strFilePath 结果文件全路径名; 

返回:成功返回true. 
注意:导出影像数据集. 
"""

#将函数库的路径添加到环境变量
sys.path.append(r"./smu/Bin")

#导入SuperMap模块
import smu as sm

#初始化Python组件环境;
sm.Init()

#====================================
#需要修改的参数
server=r"F:\Temp\2012-08-25\surface.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

if __name__ == '__main__':
	bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开oracle数据源
	if bOpen == 1:
		dtGrid1 = 'Dem2'
		sm.ExportRaster(odsAlias, dtGrid1, 'fileTIF', r'F:\Temp\2012-08-25\test.tif')
		sm.CloseDataSource(odsAlias)        
	else:
		print "打开数据源失败！"
	sm.Exit()#清空组件环境释放内存

