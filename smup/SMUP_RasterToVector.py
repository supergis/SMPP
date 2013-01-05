"""
栅格转矢量 
参数:
[in]string strDataSourceSrc 源数据源名称; 
[in]string strDtRaster 待转换的栅格数据集名称; 
[in]string strDataSourceDst 结果数据源名称: 
[in]string strDtVector 结果数据集名称: 
[in]string strDtType 结果数据集类型: 
 ?Point
 ?Line
 ?Region 
[in]string strFieldName 结果栅格值字段名称: 
[in]int bUseSpecifiedValue 设置是否只转换指定值; 
 ?1 设置使用指定值
 ?0 设置不使用指定值 

[in]double dSpecifiedValue 设置指定值(bSpecifiedValue为1时有效); 
[in]double dSpecifiedValueTolerance 设置指定值容限(bSpecifiedValue为1时有效); 
[in]int iSmoothMethod 光滑方法(结果为线数据集时有效); 
 ?0 B样条法
 ?1 磨角法 

[in]int iSmoothDegree 设置光滑度(结果为线数据集时有效); 
[in]int iNoValue 设置NoDATA, 默认为-9999; 
[in]int iNoValueTolerance 设置NoDATA容限; 
[in]int iThinRaster 设置转换之前是否进行栅格细化(只在转为线数据集时有效); 
 ?0 设置转换之前是进行栅格细化处理
 ?1 设置转换之前不进行栅格细化处理 

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
import smu as SuperMap #导入SuperMap模块

SuperMap.Init()#初始化Python组件环境;

#====================================
#需要修改的参数
server=r"F:\Temp\2012-08-25\rvconversion.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

def RasterToLine(dsSrc, dtRaster, dsDst, dtVector, strFieldName, iUseValue, dValue, 
                        dValueTolerence, iSmooth, iSmoothDegree,iNoData, iNoDataTolerence, iThin):

            SuperMap.RasterToVector(dsSrc, dtRaster, dsDst, dtVector, 'Line',
                                    strFieldName, iUseValue, dValue, dValueTolerence, 
                                    iSmooth, iSmoothDegree,iNoData, iNoDataTolerence, iThin)

def RasterToRegion(dsSrc, dtRaster, dsDst, dtVector, strFieldName, iUseValue, dValue, 
                        dValueTolerence,iNoData, iNoDataTolerence, iThin):

            SuperMap.RasterToVector(dsSrc, dtRaster, dsDst, dtVector, 'Region',
                                    strFieldName, iUseValue, dValue, dValueTolerence,
                                    0, 0, iNoData, iNoDataTolerence, 0)

def RasterToPoint(dsSrc, dtRaster, dsDst, dtVector, strFieldName, iUseValue, dValue, 
                        dValueTolerence, iNoData, iNoDataTolerence):

            SuperMap.RasterToVector(dsSrc, dtRaster, dsDst, dtVector, 'Point',
                                    strFieldName, iUseValue, dValue, dValueTolerence,
                                    0, 0, iNoData, iNoDataTolerence, 0)


if __name__ == '__main__':
            bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开oracle数据源
            if bOpen == 1:
                        dtVector = 'VectorResult'
                        dtRaster = 'contour_raster'
                        strFieldName = 'ResultField'
                        SuperMap.DeleteDataset(odsAlias, dtVector)
                        RasterToLine(odsAlias, dtRaster, odsAlias, dtVector, strFieldName, 
                                                0, 0, 0, 0, 2, -9999, 0, 1)
                        SuperMap.CloseDataSource(odsAlias)  
            else:
                        print "打开数据源失败！"
            SuperMap.Exit()#清空组件环境释放内存
