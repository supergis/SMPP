# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster    
#===================================

"""
���ڷ����� 
����:
[in]string strDataSourceSrc Դ����Դ����; 
[in]string strDtGridBefore ���ڷ�ǰ��դ�����ݼ�; 
[in]string strDtGridAfter ���ڷ����դ�����ݼ�; 
[in]string strDataSourceDst �������Դ����; 
[in]string strDatasetName ������ݼ�������; 

����:����ɹ�, �������ڷ�������Ԫ�ص�Ԫ��(������,������, �ھ����,�ھ����,δ�������ڷ������); 
"""

import os
import sys

#��.net�����·����ӵ���������
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") 

#����SuperMapģ��
import smu as SuperMap 

#��ʼ��Python�������;
SuperMap.Init()

#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\Temp\2012-08-25\�������.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

if __name__ == '__main__':
	#��oracle����Դ
	bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)
	if bOpen == 1:
		dtGrid1 = 'Dem2'
		dtGrid2 = 'DemData'
		SuperMap.DeleteDataset(odsAlias, 'dem22')
		L = SuperMap.CutFill(odsAlias, dtGrid1, dtGrid2,odsAlias, 'dem22')
		print L
		SuperMap.CloseDataSource(odsAlias)  
	else:
		print "������Դʧ�ܣ�"
		
		#�����������ͷ��ڴ�
		SuperMap.Exit()

