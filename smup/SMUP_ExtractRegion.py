"""
提取等值面 
参数:
[in]string strDataSourceSrc 源数据源名称; 
[in]string strDtRaster 源栅格数据集名称; 
[in]string strDataSourceDst 结果数据源名称: 
[in]string strDtVector 结果数据集名称: 
[in]double dDatumValue 基准值: 
[in]double dInterval 等值距: 
[in]double dFilterTolerance 采样过滤系数: 
[in]int iSmoothMethod 光滑方法; 
 ?-1 不处理
 ?0 B样条法
 ?1 磨角法 
[in]int iSmoothDegree 光滑程度; 

返回:成功返回true. 
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
server=r"F:/Temp/2012-08-25/表面分析.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

if __name__ == '__main__':
            sm.Init()#初始化Python组件环境;

            bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开oracle数据源
            if bOpen == 1:
                        dtRaster = 'dem2'
                        dtVector = 'dem2_v'
                        sm.DeleteDataset(odsAlias, dtVector)
                        sm.ExtractRegion(odsAlias, dtRaster, odsAlias, dtVector, 1432, 200, 0, -1, 3)
                        sm.CloseDataSource(odsAlias)        
            else:
                        print "打开数据源失败！"
            sm.Exit()#清空组件环境释放内存
