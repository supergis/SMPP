"""
���㾭γ����� 
����:
[in]string strDsAlias ����Դ����; 
[in]string strDtName ʸ�����ݼ�����; 
[in]string strFieldName �洢���������ֶ�����: 

����:�ɹ�����true. ע��:֧�ֵ����ݼ�����Region. 

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
