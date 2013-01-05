"""
查询矢量数据集，结果保存在指定数据集中 
参数:


[in]

string

strDataSourceSrc 被查询数据集所在数据源名称; 



[in]

string

strDatasetSrc 被查询数据集名称; 



[in]

string

strDataSourceDst 结果数据集所在数据源名称; 



[in]

string

strDatasetDst 结果数据集名称; 



[in]

string

strSQL 查询条件; 



[in]

string

strEncType 结果数据集编码类型;取值为: ?encBYTE
 ?encWORD
 ?enc3BYTE
 ?encDWORD 复合数据不能用此编码
 ?encDOUBLE
 ?encNONE 



[in]

string

strCursorType 查询游标类型; ?Dynamic
 ?Static 

返回:成功返回true. 
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
            dtName = 'bangongqu'
            dtNameNew = 'test12'
            strFilter = 'smid>1'
            curType = 'Dynamic'

            OpenDataSource(server, user, pwd, engType, dsAlias)
            DeleteDataset(dsAlias, dtNameNew)
            Query(dsAlias, dtName, dsAlias, dtNameNew, strFilter, encType, curType)
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

