"""
多边形内点转点数据集 
参数:
[in]string strDataSourceSrc 源数据源名称; 
[in]string strRegion 多边形数据集名称; 
[in]string strDataSourceDst 结果数据源名称; 
[in]string strPoint 结果点数据集名称; 

返回:成功返回true. 
"""

# coding: GB2312
#===================================
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #将.net组件的路径添加到环境变量
import smu as sm #导入SuperMap模块


#====================================
#需要修改的参数
server=r"F:\2012\相关文件\结果文件夹\A04070203.udb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
            sm.Init()#初始化Python组件环境;
            bOpen=sm.OpenDataSource(server,user, pwd,"sceUDB",odsAlias)#打开数据源
            if bOpen == 1:
                        dtSrc = 'NewDataset_2'
                        dtDst = dtSrc + 't'
                        sm.DeleteDataset(odsAlias, dtDst)
                        sm.RegionInnerToPoint(odsAlias, dtSrc, odsAlias, dtDst)
                        sm.CloseDataSource(odsAlias)        
            else:
                        print "打开数据源失败！"
            sm.Exit()#清空组件环境释放内存

