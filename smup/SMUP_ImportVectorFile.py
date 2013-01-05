"""
导入指定矢量文件 
参数:


[in]

string

strDsAlias 数据源别名; 



[in]

string

strDtName 结果数据集名称,若生成多个数据集,内部自动加“PLRT”等后缀; 



[in]

string

strEncType 目标数据编码类型,取值为: ?encBYTE
 ?encWORD
 ?enc3BYTE
 ?encDWORD
 ?encDOUBLE
 ?encNONE 



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



[in]

string

strMode 导入为简单数据集(或复合数据集), 取值为: ?GIS
 ?CAD 

返回:成功返回true. 注意:导入结果为新建数据集.
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
testPath="F:\\2012\\python范例程序\\Data\\ImportVectorFile\\Countries.shp"
fileType ="fileSHP"
#需要修改的参数
#=====================================

def to_udb(udb, fileType, filePath):
            isOpen=smu.OpenDataSource(udb, '', '', 'sceUDB', odsAlias)
            smu.DeleteDataset(odsAlias, dtName)
            #导入矢量文件
            bImport = smu.ImportVectorFile(odsAlias,'test', "encBYTE",fileType, filePath, "GIS")
            pass

def to_db(server, user, pwd, fileType, filePath):
            #打开数据源
            bOpen = smu.OpenDataSource(server,user,pwd,"sceOraclePlus",odsAlias)
            if bOpen == 1:
                        #导入矢量文件
                        bImport = smu.ImportVectorFile(odsAlias,'test', "encBYTE",fileType, filePath, "GIS")
                        if bImport == 1:
                                    print "导入成功"
                        else:
                                    print "导入失败！"
                                    smu.CloseDataSource(odsAlias)
            else:
                        print "打开数据源失败！"
                        smu.Exit()#清空环境，释放内存

if __name__=='__main__':
            if len(sys.argv)==2:
                        ugopath=sys.argv[1]
                        sys.path.append(ugopath)
                        import smu 
                        smu.Init()
                        pass
