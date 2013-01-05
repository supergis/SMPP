"""
多重缓冲区 
参数:
[in]string strDataSourceSrc 源数据源名称; 
[in]string strDatasetSrc 源数据集名称; 
[in]string strDataSourceDst 结果数据源名称: 
[in]string strDatasetDst 结果数据集名称: 
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

[in]string strRadius 缓冲半径字符串(用逗号隔开,如: 30,45,56); 
[in]int iLeftSide 是否是左半径(平头缓冲时,设置是否是左半径): 0- 右半径 1- 左半径 
[in]int iUnion 设置是否合并所有结果缓冲区; 
 ?0 不合并
 ?1 合并 
[in]int iSemicircleSegments 边界的平滑度[4, 200]; 
[in]int iRing 是否生成环状缓冲区; 
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

def Buffer(dsSrc, dtSrc, dsDst, dtDst, strUint, strR,  iUnion, iSegment, iRing):
            sm.BufferMulti(dsSrc, dtSrc, dsDst, dtDst, strUnit, 'Round', strR, 0, iUnion, iSegment, iRing)

def BufferLine(dsSrc, dtSrc, dsDst, dtDst, strUnit, strEndType, strR, iLeftSide, iUnion, iSegment, iRing):
            sm.BufferMulti(dsSrc, dtSrc, dsDst, dtDst, strUnit, strEndType, strR, 
                                    iLeftSide, iUnion, iSegment, iRing)


if __name__ == '__main__':
            bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开oracle数据源
            if bOpen == 1:
                        dtSrc = '国道'
                        dtDst = '国道buf'
                        strUnit = 'Meter'
                        sm.DeleteDataset(odsAlias, dtDst)
                        strDtType = sm.GetDatasetType(odsAlias, dtSrc)

                        if strDtType.lower()=='point' or strDtType.lower()=='region':
                                    print strDtType
                                    Buffer(odsAlias, dtSrc, odsAlias, dtDst, strUnit,
                                                            '30,45, 56', 0, 12, 1)
                        elif strDtType.lower()=='line':
                                    BufferLine(odsAlias, dtSrc, odsAlias, dtDst, strUnit,
                                                            'Flat', '30,45,56',1, 0,100, 1)
                        
                        sm.CloseDataSource(odsAlias)        
            else:
                        print "打开数据源失败！"
            sm.Exit()#清空组件环境释放内存

