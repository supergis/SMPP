# coding: GB2312

"""
������������ 
����:
[in]string strDataSourceSrc Դ����Դ����; 
[in]string strDatasetGrid ���ڿ����Է�����դ��������ݼ�����; 
[in]double dPointX �۲��λ��X; 
[in]double dPointY �۲��λ��Y; 
[in]double dPointZ �۲��λ��Z; 
[in]double dStartAngle �۲췽λ��ʼ�Ƕ�,����������0��,˳ʱ�뷽����ת; 
[in]double dViewAngle �۲�Ƕ�,���ֵΪ360��; 
[in]double dViewRadius �۲�뾶,-1����û������; 
[in]string strDataSourceDst �������Դ����; 
[in]string strDatasetName ��������������������ݼ�����; 

����:�ɹ�����true. 

"""

#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·����ӵ���������
import smu as sm #����SuperMapģ��

sm.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\Temp\2012-08-25\�������.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
            bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#������Դ
            if bOpen == 1:
                        dtGrid = 'Dem2'
                        x1=726628.410093674
                        y1=3140482.5278305
                        z1=2953
                        sm.DeleteDataset(odsAlias, 'dem22')
                        sm.CalculateViewShed(odsAlias, dtGrid, x1,y1,z1,0,360,-1, odsAlias, 'dem22')
                        sm.CloseDataSource(odsAlias)        
            else:
                        print "������Դʧ�ܣ�"
            sm.Exit()#�����������ͷ��ڴ�
 