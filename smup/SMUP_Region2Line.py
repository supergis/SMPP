"""
矢量面转线数据集 
参数:


[in]

string

strDataSourceSrc 源数据源名称; 



[in]

string

strDtRegion 待转换的面数据集名称; 



[in]

string

strDataSourceDst 结果数据集名称: 



[in]

string

strDtLine 结果线数据集名称: 

返回:成功返回true. 
"""

# -*- coding: cp936 -*-

import os, time
os.sys.path.append(r'E:\Develop\UGO6.1.2\01_SourceCode\Builds\Win_Solution_vc9\BinD')

from smu import *



def main():
            server = r'E:\Develop\UGO6.1\Builds\Win_Solution_vc9\BinD\test.udb'
            user=''
            pwd=''
            
            encType='encNONE'
            
            engType = 'sceUDB'
            dsAlias = 'odsAlias'
            dtName = 'New_Region'

            OpenDataSource(server, user, pwd, engType, dsAlias)
            DeleteDataset(dsAlias, dtName+'ed')
            RegionToLine(dsAlias, dtName, dsAlias, dtName+'ed')
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
