"""
计算经纬度面积 
参数:
[in]string strDsAlias 数据源名称; 
[in]string strDtName 矢量数据集名称; 
[in]string strFieldName 存储计算结果的字段名称: 

返回:成功返回true. 注意:支持的数据集类型Region. 

"""

# -*- coding: cp936 -*-

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
            dtName = 'New_Region'

            OpenDataSource(server, user, pwd, engType, dsAlias)
            ComputeGeoArea(dsAlias, dtName, 'area1')
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
