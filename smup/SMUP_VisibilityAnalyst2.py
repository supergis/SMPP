"""
�����Ŀ�����

����:
[in]string strDataSourceSrc Դ����Դ����; 
[in]string strDatasetGrid ���ڿ����Է�����դ��������ݼ�����; 
[in]double dFromPointX ��ʼ��X; 
[in]double dFromPointY ��ʼ��Y; 
[in]double dFromPointZ ��ʼ��Z; 
[in]double dToPointX ��ֹ��X; 
[in]double dToPointY ��ֹ��Y; 
[in]double dToPointZ ��ֹ��Z; 
[in]string strDtName ������ݼ�����; 

����:�ɹ�����true. 

ע��:
�����Խ�����ݼ��洢�����߶���.
����VisCodeΪ1���ǿ����߶���VisCodeΪ2���ǲ������߶���. 

"""

# coding: GB2312
#===================================
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·����ӵ���������
import smu #����SuperMapģ��


#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\Temp\2012-08-25\�������.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
            smu.Init()#��ʼ��Python�������;
            bOpen=smu.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#��oracle����Դ
            if bOpen == 1:
                        dtGrid = 'Dem2'
                        x1=726628.410093674
                        y1=3140482.5278305
                        z1=2953
                        x2=744233.1888066
                        y2=3129829.63616617
                        z2=4139
                        dtResult='dtResult'
                        smu.DeleteDataset(odsAlias, dtResult)
                        smu.VisibilityAnalyst2(odsAlias, dtGrid, x1,y1,z1,x2,y2,z2, dtResult)
                        smu.CloseDataSource(odsAlias)       
            else:
                        print "������Դʧ�ܣ�"
            smu.Exit()#�����������ͷ��ڴ�
