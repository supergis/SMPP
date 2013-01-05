"""
���������� 
����:


[in]

string

strDsAlias ����Դ����; 



[in]

string

strDtName ���ݼ�����; 

����:�ɹ�����true. 
"""

# coding: GB2312

#===================================
import os
import sys
#====================================

def help():
            strhelp='''
����������
1. udb����Դ
BuildPyramid.py [Bin] [udb] [dtName]

2. oracle����Դ
BuildPyramid.py [Bin] [server] [user] [pwd] [dtName]

3. dtNameΪ��ʱ, ���Ե�һ�����ݼ�����������
            '''
            return strhelp

def main(server, user, pwd, engtype, dtName):
            odsAlias="oracle"
            bOpen=smu.OpenDataSource(server,user, pwd, engtype,odsAlias)
            if bOpen == 1:
                        if dtName=="''":
                                    dtName=smu.GetDatasetName(odsAlias, 0)
                        bBuild=smu.BuildPyramid(odsAlias,dtName)#����Ӱ�������
                        if bBuild == 1:
                                    print "�����������ɹ�"
                        else:
                                    print "����Ӱ�������ʧ�ܣ�"
                        smu.CloseDataSource(odsAlias)
            else:
                        print "������Դʧ�ܣ�"
            
            smu.Exit()#�����������ͷ��ڴ�

def udb(server, dtName):
            main(server, '', '', 'sceUDB', dtName)

def oracle(server, user, pwd, dtName):
            main(server, user, pwd, 'sceOraclePlus', dtName)


if __name__=='__main__':
            if len(sys.argv) >= 4:
                        ugo = sys.argv[1]
                        sys.path.append(ugo) #��.net�����·����ӵ���������
                        import smu
            else:
                        print help()
                        sys.exit()

            print len(sys.argv), sys.argv
            if len(sys.argv)==4:
                        server=sys.argv[2]
                        dtname=sys.argv[3]
                        udb(server, dtname)
            elif len(sys.argv)==6:
                        server=sys.argv[2]
                        user=sys.argv[3]
                        pwd=sys.argv[4]
                        dtname=sys.argv[5]
                        oracle(server, user, pwd, dtname)
