"""
׷��Ӱ���ļ������ݼ������Ա���ɫ 
����:


[in]

string

strAlias ����Դ����; 



[in]

string

strName ���ݼ�����; 



[in]

string

strType �ļ�����,ȡֵΪ: ?fileTIF
 ?fileIMG
 ?fileBMP
 ?fileJPG
 ?fileGRD
 ?fileRAW
 ?fileUSGSGRID
 ?fileSIT
 ?fileArcinfoGrid
 ?fileIDR 



[in]

string

strFilePath �ļ�ȫ·����; 



[in]

int

iRed ��������ɫR; 



[in]

int

iGreen ��������ɫG; 



[in]

int

iBlue ��������ɫB; 

����:�ɹ�����true. ע��:���Ѵ������ݼ���׷��Ӱ���ļ�,����Χ�޽���,��׷��. 
ʹ��AppendRasterFile׷�ӵ���Ӱ���ļ�ʾ�� 

"""

# coding: GB2312

#===================================================
#Ӱ���������SuperMap UDB��ʽ����.
#��������:
#1��ɨ��Ŀ¼�����߸��ݾ�γ�Ȱ��տ�ĸ߿������ļ��б�
#2��ɨ����ڵ��ļ�����ȡ�������귶Χ��
#3��ɨ����ڵ��ļ�����ȡ���ظ�ʽ��
#4�������ļ��б����ڴ��ڵ��ļ�׷�ӵ��򿪵����ݿ�UDB�С�
#5�������������������Լӿ���ʾ�ٶȡ�����ѡ�Ĺ��̣�
#===================================================

import sys
import string
import re
import os
import time

def getType(ext):
            if ext.lower() == 'tif':
                        return 'fileTIF'
            elif ext.lower() == 'img':
                        return 'fileIMG'



#ƥ��������ʽ������������append��datafiles������׷��    
def walkPath(type, path):
            datafiles = []
            reMatch = '[\d\D]*.tif$'
            if type=='img':
                        reMath = '[\d\D]*.img$'
            
            for root, dirs, files in os.walk(path):
                        for file in files:
                                    if (re.match(reMatch,file)):
                                                datafiles.append(os.path.join(root, file))
            return datafiles

def calcDatasetInfo(type, datafiles):
            L=[]        
            left=[]
            top=[]
            right=[]
            bottom=[]
            ratiox=[]
            ratioy=[]

            #��ȡÿ��Ӱ���ļ������ҵ���Χ�����浽����
            for file in datafiles:
                        L= smu.GetImageGeoRef(type,file)
                        print L
                        l=float(L[0][0])
                        t=float(L[0][1])
                        r=float(L[0][2])
                        b=float(L[0][3])
                        w=int(L[1][0])
                        h=int(L[1][1])
                        x=(r-l)/w
                        y=(t-b)/h
                        
                        left.append(l)
                        right.append(r)
                        top.append(t)
                        bottom.append(b)
                        ratiox.append(x)
                        ratioy.append(y)

                        #��ȡ�������±߽�
                        dLeft=min(left)
                        dRight=max(right)
                        dTop=max(top)
                        dBottom=min(bottom)
                        
                        #��ȡ�ֱ��ʣ�Ӱ����С�ֱ�����Ϊ���ݼ��ֱ���
                        dRatioX = min(ratiox)
                        dRatioY = min(ratioy)
                        
                        #����Ӱ�����ݼ���Ⱥ͸߶�
                        nWidth = int((dRight-dLeft)/dRatioX)
                        nHeight = int((dTop-dBottom)/dRatioY)
                        
                        #���¼��㣬��֤�ֱ�����ȷ
                        dRight=dLeft+dRatioX*nWidth
                        dBottom=dTop-dRatioY*nHeight
                        L = [nWidth, nHeight, dLeft, dTop, dRight, dBottom]
            
            return L

def toDB(server, user, pwd, engType, fileType, path):
            files=[]
            files=walkPath(fileType, path)
            if len(files)>0:
                        L=[]
                        L = calcDatasetInfo(fileType, files)
                        pixType = smu.GetImagePixelFormatName(fileType, files[0])

                        odsAlias='test'
                        if len(L)==6:
                                    nWidth=L[0]
                                    nHeight=L[1]
                                    dLeft=L[2]
                                    dTop=L[3]
                                    dRight=L[4]
                                    dBottom=L[5]
                                    dtName='test'
                                    isOpen=smu.OpenDataSource(server,user,pwd, engType, odsAlias)
                                    smu.DeleteDataset(odsAlias, dtName)
                                    bCreate = smu.CreateDatasetRaster(odsAlias,dtName, 
                                                            'Image', 'encDCT', pixType,nWidth,nHeight, 
                                                            dLeft, dTop,dRight,dBottom,256)
                                    for file in files:
                                                smu.AppendRasterFile(odsAlias,dtName,fileType, file)
                                    
                                    smu.CloseDataSource(odsAlias)


#=====================================
def writeLog(logPath, tmpstr):
    time_str = time.strftime("%Y-%m-%d %H:%M:%S ",time.localtime())
    logstr = str(tmpstr) + time_str +'\n'
    print(logstr)
    f = open(logPath, "a")
    f.write(logstr)
    f.close()


help =u"----------------------------------------------------------\n\
˵��:�ɵ���udb��oracle����\n\
���뵽UDB�÷�: AppendRasterFile.py ugoPath tif c:/data\n\
���뵽Oracle�÷�: AppendRasterFile.py ugoPath server user pwd tif c:/data\n\
----------------------------------------------------------\n"

if __name__=='__main__':
            if len(sys.argv)>2:
                        ugo=sys.argv[1]
                        if os.path.exists(ugo):
                                    sys.path.append(ugo)
                                    import smu
                        else:
                                    print u'���·��������.'
                                    sys.exit()
            else:
                        print help
                        sys.exit()

            if len(sys.argv) == 4:
                        engType='sceUDB'
                        fileType=sys.argv[2]
                        fileType=getType(fileType)
                        path=sys.argv[3]
                        
                        udb = path+'/test.udb'
                        udd = path+'/test.udd'
                        if os.path.exists(udb):
                                    os.remove(udb)
                        if os.path.exists(udd):
                                    os.remove(udd)

                        toDB(udb, '', '', engType, fileType, path)
                        smu.Exit()#��ջ������ͷ��ڴ�
            elif len(sys.argv) == 7:
                        engType='sceOraclePlus'
                        server=sys.argv[2]
                        user=sys.argv[3]
                        pwd=sys.argv[4]
                        fileType=sys.argv[5]
                        fileType=getType(fileType)
                        path=sys.argv[6]
                        toDB(server, user, pwd, engType, fileType, path)
                        smu.Exit()#��ջ������ͷ��ڴ�
