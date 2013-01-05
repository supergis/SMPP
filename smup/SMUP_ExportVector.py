"""
导出为矢量文件 
参数:
[in]string strDsAlias 数据源别名; 
[in]string strName 矢量数据集名称; 
[in]string strType 文件类型, 取值为: 
 ?fileAIBinCov
 ?fileE00
 ?fileSHP
 ?fileTAB
 ?fileMIF
 ?fileDGN
 ?fileDWG
 ?fileDXF
 ?fileGML
 ?fileMAPGIS
 ?fileKML
 ?fileKMZ 

[in]string strFilePath 结果文件全路径名; 

返回:成功返回true. 注意:导出矢量数据集. 

"""

# coding: GB2312
#===================================
#向指定的数据集追加数据集
#AppendDatasetRaster    
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #将.net组件的路径添加到环境变量
import smu as sm #导入SuperMap模块


#====================================
#需要修改的参数
server=r"F:\Temp\2012-08-25\表面分析.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
            sm.Init()#初始化Python组件环境;

            bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开oracle数据源
            if bOpen == 1:
                        dtName = 'Dem2'
                        sm.ExportRaster(odsAlias, dtName, 'fileSHP', r'F:\Temp\2012-08-25\test.shp')
                        sm.CloseDataSource(odsAlias)        
            else:
                        print "打开数据源失败！"
            sm.Exit()#清空组件环境释放内存
