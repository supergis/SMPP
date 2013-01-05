# coding: GB2312

"""
单点可视域分析 
参数:
[in]string strDataSourceSrc 源数据源名称; 
[in]string strDatasetGrid 用于可视性分析的栅格表面数据集名称; 
[in]double dPointX 观察点位置X; 
[in]double dPointY 观察点位置Y; 
[in]double dPointZ 观察点位置Z; 
[in]double dStartAngle 观察方位起始角度,以正北方向0度,顺时针方向旋转; 
[in]double dViewAngle 观察角度,最大值为360度; 
[in]double dViewRadius 观测半径,-1代表没有限制; 
[in]string strDataSourceDst 结果数据源名称; 
[in]string strDatasetName 可视域分析结果保存的数据集名称; 

返回:成功返回true. 

"""

#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #将.net组件的路径添加到环境变量
import smu as sm #导入SuperMap模块

sm.Init()#初始化Python组件环境;

#====================================
#需要修改的参数
server=r"F:\Temp\2012-08-25\表面分析.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
            bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开数据源
            if bOpen == 1:
                        dtGrid = 'Dem2'
                        x1=726628.410093674
                        y1=3140482.5278305
                        z1=2953
                        sm.DeleteDataset(odsAlias, 'dem22')
                        sm.CalculateViewShed(odsAlias, dtGrid, x1,y1,z1,0,360,-1, odsAlias, 'dem22')
                        sm.CloseDataSource(odsAlias)        
            else:
                        print "打开数据源失败！"
            sm.Exit()#清空组件环境释放内存
 