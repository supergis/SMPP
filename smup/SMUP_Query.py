"""
��ѯʸ�����ݼ������������ָ�����ݼ��� 
����:


[in]

string

strDataSourceSrc ����ѯ���ݼ���������Դ����; 



[in]

string

strDatasetSrc ����ѯ���ݼ�����; 



[in]

string

strDataSourceDst ������ݼ���������Դ����; 



[in]

string

strDatasetDst ������ݼ�����; 



[in]

string

strSQL ��ѯ����; 



[in]

string

strEncType ������ݼ���������;ȡֵΪ: ?encBYTE
 ?encWORD
 ?enc3BYTE
 ?encDWORD �������ݲ����ô˱���
 ?encDOUBLE
 ?encNONE 



[in]

string

strCursorType ��ѯ�α�����; ?Dynamic
 ?Static 

����:�ɹ�����true. 
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

