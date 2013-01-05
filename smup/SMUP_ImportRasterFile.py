"""
导入指定影像文件 
参数:
[in]string strDsAlias 数据源别名; 
[in]string strName 数据集名称; 
[in]string strEncType 目标数据编码类型,取值为: 
 ?encNONE
 ?encDCT
 ?encSGL
 ?encLGL
 ?encLZW
 ?encCompound 

[in]string strType 文件类型, 取值为: ?fileTIF
 ?fileIMG
 ?fileBMP
 ?fileJPG
 ?fileGRD
 ?fileRAW
 ?fileUSGSGRID
 ?fileSIT
 ?fileArcInfoGrid
 ?fileIDR
 ?fileGDBRaster 

[in]string strFilePath 文件全路径名; 
[in]int iGrid 可选参数,是否导入为GRID数据集,默认为false. 

返回:成功返回true. 
注意:导入结果为新建数据集. 

"""

# coding: GB2312

import sys
sys.path.append(r'E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD')
import string
import re
import smu
import os
import time

def getType(ext):
            print ext
            if ext.lower() == 'tif':
                        fileType='fileTIF'
            elif ext.lower() == 'img':
                        fileType='fileIMG'

            return fileType


def toUDB(file):
            iPos = file.find('.')
            ext = file[iPos+1:len(file)]
            fileType = 'fileTIF'
            fileType = getType(ext) 
            
            udb = file[0:iPos+1]+'udb'
            udd = file[0:iPos+1]+'udd'
            if os.path.exists(udb):
                        os.remove(udb)
            if os.path.exists(udd):
                        os.remove(udd)
            
            odsAlias='test'
            if smu.CreateDataSource(udb, '', '', 'sceUDB', odsAlias):
                        if smu.ImportRasterFile(odsAlias, 't', 'encDCT', fileType, file):
                                    print '导入成功:', udb
                        else:
                                    print '导入失败:', file



def toDB(server, user, pwd, file):
            iPos = file.find('.')
            ext = file[iPos+1:len(file)]
            fileType = getType(ext)

            odsAlias = 'test'
            if smu.OpenDataSource(server, user, pwd, 'sceOraclePlus', odsAlias):
                        dtName='t'
                        smu.DeleteDataset(odsAlias, dtName)
                        if smu.ImportRasterFile(odsAlias, dtName, 'encDCT', fileType, file):
                                    print '导入成功:', file
                        else:
                                    print '导入失败:', file


if __name__=='__main__':
            if len(sys.argv)==2:
                        file = sys.argv[1]
                        toUDB(file)
                        smu.Exit()
            elif len(sys.argv)==5:
                        server=sys.argv[1]
                        user=sys.argv[2]
                        pwd=sys.argv[3]
                        file=argv[4]
                        toDB(server, user, pwd, file)
                        smu.Exit()
            
