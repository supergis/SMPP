# coding: GB2312
import sys
import string
import re
import os
import time

print "��ӭʹ�ó�ͼ����ռ���Ϣͨ�ô���ϵͳ-SMUP."
print "Welcome to SuperMap Universal Processor."

SMU_Path="..\\SMU\\"
sys.path.append(SMU_Path)
import smu

#��ʾ�汾��Ϣ
def SMUP_Version():
	print "SuperMap Universal Processor.","V2012.11.28"
	print "Copyright,SuperMap GIS Inc,GIS Institute."
	print "Author: SJ Li,EQ Wang,WY lin,Q Huang,SW Teng. 2012"

def SMUP_List():
	print "SMUP_List"
	
#��ʼ��
def SMUP_Init():
	sys.path.append(SMU_Path)
	import smu

#��ջ������ͷ��ڴ�	
def SMUP_Close():
	smu.Exit()	



#=====================================
def writeLog(logPath, tmpstr):
    time_str = time.strftime("%Y-%m-%d %H:%M:%S	",time.localtime())
    logstr = str(tmpstr) + time_str +'\n'
    print(logstr)
    f = open(logPath, "a")
    f.write(logstr)
    f.close()