# coding: GB2312
#===================================
#��������Դ
#CreateDataSource       
#===================================
import os
import sys
sys.path.append(r'..\..\Bin') #�������·����ӵ���������
import smu as SuperMap #���� SuperMap ģ��

SuperMap.Init()#��ʼ�� Python �������;

#====================================
#��Ҫ�޸ĵĲ������� UDBPlus ����ԴΪ��
server=r"..\..\SampleData\Python\udbTest" 
user=""
password=""
alias="UDBPlus"
#====================================

isCreate=SuperMap.CreateDataSource(server,user,password,"sceUDB",alias)
if isCreate == 1:
    print "�½�����Դ�ɹ���"
else:
    print "�½�����Դʧ�ܣ�"
    
SuperMap.Exit()#�����������ͷ��ڴ�
