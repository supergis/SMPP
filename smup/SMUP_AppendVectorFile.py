"""
׷��ʸ���ļ���ָ�����ݼ� 
����:


[in]

string

strDsAlias ����Դ����; 



[in]

string

strDtName Ŀ�����ݼ�����; 



[in]

string

strType �ļ�����, ȡֵΪ: ?fileAIBinCov
 ?fileE00
 ?fileSHP
 ?fileTAB
 ?fileMIF
 ?fileDGN
 ?fileDWG
 ?fileDXF
 ?fileGML
 ?fileMAPGIS
 ?fileKML
 ?fileKMZ
 ?fileGDBVector 



[in]

string

strFilePath �ļ�ȫ·����; 

����:�ɹ�����true. ע��:���뵽ָ�����Ƶ����ݼ���.
"""

# coding: GB2312

import sys
import string
import re
import os
import time


#=====================================
#��Ҫ�޸ĵĲ���  
odsAlias="odsAlias"
#��Ҫ�޸ĵĲ���
#=====================================


#ƥ��������ʽ������������append��datafiles������׷��    
def walkPath(type, path):
            datafiles = []
            reMatch = '[\d\D]*.shp$'
            if type=='shp':
                        reMath = '[\d\D]*.shp$'
            
            for root, dirs, files in os.walk(path):
                        for file in files:
                                    if (re.match(reMatch,file)):
                                                datafiles.append(os.path.join(root, file))
            return datafiles



def getType(ext):
            if ext.lower() == 'shp':
                        return 'fileSHP'


def to_udb(udb, dtName, fileType, path):
            files = walkPath(fileType, path)    
            isOpen=smu.OpenDataSource(udb, '', '', 'sceUDB', odsAlias)
            if isOpen and len(files)>0:
                        fileType = getType(fileType)
                        for file in files:
                                    #����ʸ���ļ�
                                    smu.AppendVectorFile(odsAlias, dtName, fileType, file)
            
            smu.CloseDataSource(odsAlias)

if __name__=='__main__':
            if len(sys.argv)==6:
                        ugopath=sys.argv[1]
                        sys.path.append(ugopath)
                        print sys.path
			
                        import smu
                        udb=sys.argv[2] #r'F:\Temp\2012-02-24\test.udb'
                        dtName=sys.argv[3] #'����0'
                        type=sys.argv[4]
                        dirPath=sys.argv[5] #r'D:\testdata\�������ο�������\����0_Xian80'
                        to_udb(udb, dtName, type, dirPath)
