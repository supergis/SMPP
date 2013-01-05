"""
缓冲区 
参数:
[in]string strDataSourceSrc 源数据源名称; 
[in]string strDatasetSrc 源数据集名称; 
[in]string strDataSourceDst 结果数据源名称: 
[in]string strDatasetDst 结果数据集名称: 
[in]double dLeftDistance 左缓冲区的距离(源数据集为点,面时,左右缓冲半径应一致): 
[in]double dRightDistance 右缓冲区的距离(源数据集为点,面时,左右缓冲半径应一致); 
[in]string strUnit 缓冲半径单位; 
 ?MiliMeter 毫米
 ?CentiMeter 厘米
 ?DeciMeter 分米
 ?Meter 米
 ?KiloMeter 千米
 ?Yard 码
 ?Inch 英寸
 ?Foot 英尺
 ?Mile 英里 
[in]string strEndType 端点类型(线数据集时有效); 
 ?Round 圆头缓冲
 ?Flat 平头缓冲 
[in]int iUnion 设置是否合并所有结果缓冲区; 
 ?0 不合并
 ?1 合并 
[in]int iSemicircleSegments 边界的平滑度[4, 200]; 
[in]string strFilter 过滤条件, 可选参数; 

返回:成功返回true. 
"""

# coding: GB2312
#===================================
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #将.net组件的路径添加到环境变量
import smu as sm #导入SuperMap模块

sm.Init()#初始化Python组件环境;

#====================================
#需要修改的参数
server=r"F:\Temp\2012-08-25\辽宁3.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

def Buffer(dsSrc, dtSrc, dsDst, dtDst, dDistance,strUnit, iUnion, iSegment):
            sm.Buffer(dsSrc, dtSrc, dsDst, dtDst, dDistance, 
                                    dDistance, strUnit, 'Round', iUnion, iSegment)

def BufferLine(dsSrc, dtSrc, dsDst, dtDst, dLeft, dRight, strUnit, 
                        strEndType, iUnion, iSegment):
            sm.Buffer(dsSrc, dtSrc, dsDst, dtDst, dLeft, dRight, 
                        strUnit, strEndType, iUnion, iSegment)


if __name__ == '__main__':
            bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开oracle数据源
            if bOpen == 1:
                        dtSrc = '国道'
                        dtDst = '国道buf'
                        strUnit = 'Meter'
                        sm.DeleteDataset(odsAlias, dtDst)
                        strDtType = sm.GetDatasetType(odsAlias, dtSrc)

                        if strDtType.find('Point')!=-1 or strDtType.find('Region')!=-1:
                                    print strDtType
                                    Buffer(odsAlias, dtSrc, odsAlias, dtDst, 10, strUnit, 0, 12)
                        elif strDtType.find('')!=-1:
                                    BufferLine(odsAlias, dtSrc, odsAlias, dtDst, 10, 10,
                                                            strUnit, 'Flat', 0, 100)
                        
                        sm.CloseDataSource(odsAlias)        
            else:
                        print "打开数据源失败！"
            sm.Exit()#清空组件环境释放内存
