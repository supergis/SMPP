"""
������ڵ�ת�����ݼ� 
����:
[in]string strDataSourceSrc Դ����Դ����; 
[in]string strRegion ��������ݼ�����; 
[in]string strDataSourceDst �������Դ����; 
[in]string strPoint ��������ݼ�����; 

����:�ɹ�����true. 
"""

# coding: GB2312
#===================================
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·����ӵ���������
import smu as sm #����SuperMapģ��


#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\2012\����ļ�\����ļ���\A04070203.udb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
            sm.Init()#��ʼ��Python�������;
            bOpen=sm.OpenDataSource(server,user, pwd,"sceUDB",odsAlias)#������Դ
            if bOpen == 1:
                        dtSrc = 'NewDataset_2'
                        dtDst = dtSrc + 't'
                        sm.DeleteDataset(odsAlias, dtDst)
                        sm.RegionInnerToPoint(odsAlias, dtSrc, odsAlias, dtDst)
                        sm.CloseDataSource(odsAlias)        
            else:
                        print "������Դʧ�ܣ�"
            sm.Exit()#�����������ͷ��ڴ�

