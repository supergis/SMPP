"""
两点间的可视性 
参数:
[in]string strDataSourceSrc 源数据源名称; 
[in]string strDatasetGrid 用于可视性分析的栅格表面数据集名称; 
[in]double dFromPointX 起始点X; 
[in]double dFromPointY 起始点Y; 
[in]double dFromPointZ 起始点Z; 
[in]double dToPointX 终止点X; 
[in]double dToPointY 终止点Y; 
[in]double dToPointZ 终止点Z; 

返回:通视返回空元组,否则返回第一阻视点元组(X,Y,Z). 
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
server=r"F:\Temp\2012-08-25\表面分析.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
            bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开oracle数据源
            if bOpen == 1:
                        dtGrid = 'Dem2'
                        x1=726628.410093674
                        y1=3140482.5278305
                        z1=2953
                        x2=744233.1888066
                        y2=3129829.63616617
                        z2=4139
                        L = SuperMap.VisibilityAnalyst(odsAlias, dtGrid, x1,y1,z1,x2,y2,z2)
                        print L
                        SuperMap.CloseDataSource(odsAlias)  
            else:
                        print "打开数据源失败！"
            SuperMap.Exit()#清空组件环境释放内存
