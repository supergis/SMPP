"""
ֻ������������ 
����:
[in]string strDsAlias ����Դ����; 
[in]string strDtName ���ݼ�����; 

����:�ɹ�����true. 
ע��:
Ϊ�´�����Ӱ�����ݼ�����������; 
ֻ�����������㣬�������������������. 
�˷����ŵ�����,������ΧӰ�����ݼ�,������׷�����ݳ���;�ɴ���Լʱ��. 
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
dtName="UGCIMAGE_TF_NoValue"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#��oracle����Դ
if bOpen == 1:
    bBuild=SuperMap.BuildPyramidTiersOnly(odsAlias,dtName)#����Ӱ�������
    if bBuild == 1:
        print "�����������ɹ�"
    else:
        print "����Ӱ�������ʧ�ܣ�"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "������Դʧ�ܣ�"

SuperMap.Exit()#�����������ͷ��ڴ�
