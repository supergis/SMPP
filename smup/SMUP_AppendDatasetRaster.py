"""
��ָ�������ݼ�׷��Ӱ�����ݼ� 
����:


[in]

string

strDataSourceSrc Դ����Դ����; 



[in]

string

strDatasetSrc Դ���ݼ�����; 



[in]

string

strDataSourceDst ��׷������Դ����; 



[in]

string

strDatasetDst ��׷�����ݼ�����; 

����:�ɹ�����true; ע��:���Ѵ������ݼ���׷��Ӱ�����ݼ�. 
"""

# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster    
#===================================
import os
import sys
sys.path.append(r"D:\DotNetPythonBin\Bin") #��.net�����·����ӵ���������
import smu as SuperMap #����SuperMapģ��

SuperMap.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ�������Oracle����ԴΪ��
server="sfc60" 
user="testMTT"
pwd="testMTT"
odsAlias="oracle"
strDatasetSrc="DatasetSrc"
strDatasetDst="DatasetDst"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#��oracle����Դ
if bOpen == 1:
    bAppend=SuperMap.AppendDatasetRaster(odsAlias,strDatasetSrc,odsAlias,strDatasetDst)#׷�����ݼ�
    if bAppend == 1:
        print "׷�����ݼ��ɹ�"
    else:
        print "׷��ʧ�ܣ�"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "������Դʧ�ܣ�"
    
SuperMap.Exit()#�����������ͷ��ڴ�
