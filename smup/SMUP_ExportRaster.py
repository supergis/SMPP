# coding: GB2312
#===================================

import os
import sys

"""
����ΪӰ���ļ� 
����:
[in]string strDsAlias ����Դ����; 
[in]string strName Ӱ�����ݼ�����; 
[in]string strType �ļ�����, ȡֵΪ: 
 ?fileTIF
 ?fileIMG
 ?fileBMP
 ?fileJPG
 ?filePNG
 ?fileSIT 
[in]string strFilePath ����ļ�ȫ·����; 

����:�ɹ�����true. 
ע��:����Ӱ�����ݼ�. 
"""

#���������·����ӵ���������
sys.path.append(r"./smu/Bin")

#����SuperMapģ��
import smu as sm

#��ʼ��Python�������;
sm.Init()

#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\Temp\2012-08-25\surface.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

if __name__ == '__main__':
	bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#��oracle����Դ
	if bOpen == 1:
		dtGrid1 = 'Dem2'
		sm.ExportRaster(odsAlias, dtGrid1, 'fileTIF', r'F:\Temp\2012-08-25\test.tif')
		sm.CloseDataSource(odsAlias)        
	else:
		print "������Դʧ�ܣ�"
	sm.Exit()#�����������ͷ��ڴ�

