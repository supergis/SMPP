# coding: GB2312
#===================================
#===================================
import os
import sys

#将.net组件的路径添加到环境变量
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") 

#导入SuperMap模块
import smu as sm

if __name__ == '__main__':
	sm.Init()#初始化Python组件环境;
	bResult = sm.ExportMapToFile(r'F:\Temp\2012-08-25\test.smwu', 'test', 'fileTIF', r'F:\Temp\2012-08-25\test.tif')

	if bResult == 1:
		print '操作成功.'
	else:
		print '操作失败.'

        sm.Exit()#清空组件环境释放内存
