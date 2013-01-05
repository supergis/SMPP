# coding: GB2312
#===================================
#向指定的数据集追加数据集
#AppendDatasetRaster    
#===================================

"""
填挖方计算 
参数:
[in]string strDataSourceSrc 源数据源名称; 
[in]string strDtGridBefore 填挖方前的栅格数据集; 
[in]string strDtGridAfter 填挖方后的栅格数据集; 
[in]string strDataSourceDst 结果数据源名称; 
[in]string strDatasetName 结果数据集的名称; 

返回:计算成功, 返回填挖方结果五个元素的元组(填充面积,填充体积, 挖掘面积,挖掘体积,未进行填挖方的面积); 
"""

import os
import sys

#将.net组件的路径添加到环境变量
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") 

#导入SuperMap模块
import smu as SuperMap 

#初始化Python组件环境;
SuperMap.Init()

#====================================
#需要修改的参数
server=r"F:\Temp\2012-08-25\表面分析.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

if __name__ == '__main__':
	#打开oracle数据源
	bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)
	if bOpen == 1:
		dtGrid1 = 'Dem2'
		dtGrid2 = 'DemData'
		SuperMap.DeleteDataset(odsAlias, 'dem22')
		L = SuperMap.CutFill(odsAlias, dtGrid1, dtGrid2,odsAlias, 'dem22')
		print L
		SuperMap.CloseDataSource(odsAlias)  
	else:
		print "打开数据源失败！"
		
		#清空组件环境释放内存
		SuperMap.Exit()

