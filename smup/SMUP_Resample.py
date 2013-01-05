# -*- coding: cp936 -*-

"""
对矢量数据集重采样 
参数:
[in]string strDsAlias 数据源名称; 
[in]string strDtName 待采样矢量数据集名称; 
[in]string strResampleType 采样算法: 
 ?RTBend 逐点采样算法
 ?RTGeneral 道格拉斯算法 

[in]double dTolerance 重采样的容限值，默认值为1e-10 

注意:支持的数据集类型Line, Network, Region. 返回:成功返回true. 

"""


import os, time
os.sys.path.append(r'E:\Develop\UGO6.1.2\01_SourceCode\Builds\Win_Solution_vc9\BinD')

from smu as SuperMap import *

def main():
            server = r'E:\Develop\UGO6.1\Builds\Win_Solution_vc9\BinD\test.udb'
            user=''
            pwd=''
            
            encType='encNONE'
            
            engType = 'sceUDB'
            dsAlias = 'odsAlias'
            dtName = 'New_Line'

            OpenDataSource(server, user, pwd, engType, dsAlias)
            Resample(dsAlias, dtName, 'RTBend', 15.2)
            CloseDataSource(dsAlias)

def printTime():
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print time_str

if __name__ =='__main__':
            Init()
            printTime()
            main()
            printTime()
            Exit()

