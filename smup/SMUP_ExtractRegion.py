"""
��ȡ��ֵ�� 
����:
[in]string strDataSourceSrc Դ����Դ����; 
[in]string strDtRaster Դդ�����ݼ�����; 
[in]string strDataSourceDst �������Դ����: 
[in]string strDtVector ������ݼ�����: 
[in]double dDatumValue ��׼ֵ: 
[in]double dInterval ��ֵ��: 
[in]double dFilterTolerance ��������ϵ��: 
[in]int iSmoothMethod �⻬����; 
 ?-1 ������
 ?0 B������
 ?1 ĥ�Ƿ� 
[in]int iSmoothDegree �⻬�̶�; 

����:�ɹ�����true. 
"""

# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster    
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·����ӵ���������
import smu as sm #����SuperMapģ��


#====================================
#��Ҫ�޸ĵĲ���
server=r"F:/Temp/2012-08-25/�������.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

if __name__ == '__main__':
            sm.Init()#��ʼ��Python�������;

            bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#��oracle����Դ
            if bOpen == 1:
                        dtRaster = 'dem2'
                        dtVector = 'dem2_v'
                        sm.DeleteDataset(odsAlias, dtVector)
                        sm.ExtractRegion(odsAlias, dtRaster, odsAlias, dtVector, 1432, 200, 0, -1, 3)
                        sm.CloseDataSource(odsAlias)        
            else:
                        print "������Դʧ�ܣ�"
            sm.Exit()#�����������ͷ��ڴ�
