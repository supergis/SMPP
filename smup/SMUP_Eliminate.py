"""
�����ݼ������κϲ� 
����:
[in]string strDataSourceSrc Դ����Դ����; 
[in]string strRegion ���ϲ����ݼ�����; 
[in]double dAreaTolerance ���������,С�ڴ�����Ķ���ν��ᱻ�ϲ�; 
[in]double dVertexTolerance �ڵ�����; 
[in]int iMode �ϲ�ģʽ����; 
 ?1 EliminateByArea ������ϲ�
 ?2 EliminateByBorder �������߽�ϲ� 
[in]int iDeleteSingleRegion �Ƿ��Զ�ɾ��������С�����; 

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
import smu as SuperMap #����SuperMapģ��

SuperMap.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\Temp\2012-08-25\��ͼ�ۺ�.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
            bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#��oracle����Դ
            if bOpen == 1:
                        dtSrc = 'county'
                        SuperMap.Eliminate(odsAlias, dtSrc, 134591789, 0, 1, 0)
                        SuperMap.CloseDataSource(odsAlias)  
            else:
                        print "������Դʧ�ܣ�"
            SuperMap.Exit()#�����������ͷ��ڴ�
