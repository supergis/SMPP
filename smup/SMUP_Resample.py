# -*- coding: cp936 -*-

"""
��ʸ�����ݼ��ز��� 
����:
[in]string strDsAlias ����Դ����; 
[in]string strDtName ������ʸ�����ݼ�����; 
[in]string strResampleType �����㷨: 
 ?RTBend �������㷨
 ?RTGeneral ������˹�㷨 

[in]double dTolerance �ز���������ֵ��Ĭ��ֵΪ1e-10 

ע��:֧�ֵ����ݼ�����Line, Network, Region. ����:�ɹ�����true. 

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

