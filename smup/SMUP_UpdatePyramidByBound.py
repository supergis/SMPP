# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster    
#===================================

"""
��ָ����Χ����Ӱ������� 
����:
[in]string dsAlias Ӱ�����ݼ���������Դ����; 
[in]string dtName Ӱ�����ݼ�����; 
[in]double dleft ָ����Χleft; 
[in]double dtop ָ����Χtop; 
[in]double dright ָ����Χright; 
[in]double dbottom ָ����Χbottom; 

����:�ɹ�����true. 
ע��:�ɴﵽ�ֲ����½�����Ŀ�ģ���һ����ΧӰ��׷������ʱ�������ؽ��������� 
"""

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
dtName="UpdatePyramidByBound"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#��oracle����Դ
if bOpen == 1:
    dLeft=0
    dTop=1537
    dRight=1728
    dBottom=0
    bBuild=SuperMap.UpdatePyramidByBound(odsAlias,dtName,dLeft,dTop,dRight,dBottom)#����Ӱ�������
    if bBuild == 1:
        print "����Ӱ��������ɹ���"
    else:
        print "����Ӱ�������ʧ�ܣ�"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "������Դʧ�ܣ�"

SuperMap.Exit()#�����������ͷ��ڴ�
