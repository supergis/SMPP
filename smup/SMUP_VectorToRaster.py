# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster    
#===================================

"""
ʸ��תդ�� 
����:
[in]string strDataSourceSrc Դ����Դ����; 
[in]string strDtVector ��ת����ʸ�����ݼ�����; 
[in]string strDataSourceDst �������Դ����: 
[in]string strDtRaster ���դ�����ݼ�����: 
[in]string strFieldName դ��ֵ�ֶ�����: 
[in]int iPixelFormat ���դ�����ظ�ʽ, ȡֵΪ: 
 ?8 IPF_BYTE
 ?16 IPF_TBYTE
 ?24 IPF_RGB
 ?32 IPF_RGBA
 ?320 IPF_LONG
 ?3200 IPF_FLOAT
 ?6400 IPF_DOUBLE 

[in]double dResolution ���դ��ֱ���,����Ϊ0ʱ,ʹ���ڲ�Ĭ�ϼ���ֵ: 

����:�ɹ�����true. 

"""

import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·����ӵ���������
import smu as SuperMap #����SuperMapģ��

SuperMap.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\Temp\2012-08-25\rvconversion.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#��oracle����Դ
if bOpen == 1:
            dtRaster = 'DQ35_Raster'
            SuperMap.DeleteDataset(odsAlias, dtRaster)
            SuperMap.VectorToRaster(odsAlias, 'DQ36', odsAlias, dtRaster, 'SmUserID', 320, 933)
            SuperMap.CloseDataSource(odsAlias)  
else:
    print "������Դʧ�ܣ�"
    
SuperMap.Exit()#�����������ͷ��ڴ�
