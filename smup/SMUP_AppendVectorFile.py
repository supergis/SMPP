"""
追加矢量文件到指定数据集 
参数:


[in]

string

strDsAlias 数据源别名; 



[in]

string

strDtName 目标数据集名称; 



[in]

string

strType 文件类型, 取值为: ?fileAIBinCov
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

strFilePath 文件全路径名; 

返回:成功返回true. 注意:导入到指定名称的数据集中.
"""

# coding: GB2312

import sys
import string
import re
import os
import time


#=====================================
#需要修改的参数  
odsAlias="odsAlias"
#需要修改的参数
#=====================================


#匹配正则表达式，符合条件的append到datafiles，用于追加    
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
                                    #导入矢量文件
                                    smu.AppendVectorFile(odsAlias, dtName, fileType, file)
            
            smu.CloseDataSource(odsAlias)

if __name__=='__main__':
            if len(sys.argv)==6:
                        ugopath=sys.argv[1]
                        sys.path.append(ugopath)
                        print sys.path
			
                        import smu
                        udb=sys.argv[2] #r'F:\Temp\2012-02-24\test.udb'
                        dtName=sys.argv[3] #'区域0'
                        type=sys.argv[4]
                        dirPath=sys.argv[5] #r'D:\testdata\测评二次开发数据\区域0_Xian80'
                        to_udb(udb, dtName, type, dirPath)
