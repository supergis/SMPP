"""
Ϊָ��Ӱ�����ݼ�����NoValue. 
����:

[in]string strDsAlias ����Դ����; 
[in]string trDtName ���ݼ�����; 
[in]double dNoData NoValue; 

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
dtName="SetNoValue"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#��oracle����Դ
if bOpen == 1:
    bBuild=SuperMap.SetNoValue(odsAlias,dtName,0)#������ֵ
    if bBuild == 1:
        print "������ֵ�ɹ�"
    else:
        print "������ֵʧ��"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "������Դʧ�ܣ�"

SuperMap.Exit()#�����������ͷ��ڴ�

