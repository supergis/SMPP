"""
ΪӰ�����ݼ����òü������ 
����:


[in]

string

strDataSourceRst Ӱ�����ݼ���������Դ����; 



[in]

string

strDatasetRst Ӱ�����ݼ�����; 



[in]

string

strDataSourceVct �ü��������������Դ����; 



[in]

string

strDatasetVector �ü�������������ݼ�����; 



[in]

int

smId �ü������smid; 

ע��:�ü��������ָ����ʸ�����ݼ���.
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
dtName="SetClipRegion"
dtRName="SetClipRegion_R"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#��oracle����Դ
if bOpen == 1:
    bSetClipRegion=SuperMap.SetClipRegion(odsAlias,dtName,odsAlias,dtRName,1)#ΪӰ�����ݼ����òü������
    if SetClipRegion == 1:
        print "ΪӰ�����ݼ����òü�����γɹ�"
    else:
        print "ΪӰ�����ݼ����òü������ʧ�ܣ�"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "������Դʧ�ܣ�"

SuperMap.Exit()#�����������ͷ��ڴ�
