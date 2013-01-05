"""
���ػ����� 
����:
[in]string strDataSourceSrc Դ����Դ����; 
[in]string strDatasetSrc Դ���ݼ�����; 
[in]string strDataSourceDst �������Դ����: 
[in]string strDatasetDst ������ݼ�����: 
[in]string strUnit ����뾶��λ; 
 ?MiliMeter ����
 ?CentiMeter ����
 ?DeciMeter ����
 ?Meter ��
 ?KiloMeter ǧ��
 ?Yard ��
 ?Inch Ӣ��
 ?Foot Ӣ��
 ?Mile Ӣ�� 

[in]string strEndType �˵�����(�����ݼ�ʱ��Ч); 
 ?Round Բͷ����
 ?Flat ƽͷ���� 

[in]string strRadius ����뾶�ַ���(�ö��Ÿ���,��: 30,45,56); 
[in]int iLeftSide �Ƿ�����뾶(ƽͷ����ʱ,�����Ƿ�����뾶): 0- �Ұ뾶 1- ��뾶 
[in]int iUnion �����Ƿ�ϲ����н��������; 
 ?0 ���ϲ�
 ?1 �ϲ� 
[in]int iSemicircleSegments �߽��ƽ����[4, 200]; 
[in]int iRing �Ƿ����ɻ�״������; 
[in]string strFilter ��������, ��ѡ����; 

����:�ɹ�����true. 
"""

# coding: GB2312
#===================================
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·����ӵ���������
import smu as sm #����SuperMapģ��

sm.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\Temp\2012-08-25\����3.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

def Buffer(dsSrc, dtSrc, dsDst, dtDst, strUint, strR,  iUnion, iSegment, iRing):
            sm.BufferMulti(dsSrc, dtSrc, dsDst, dtDst, strUnit, 'Round', strR, 0, iUnion, iSegment, iRing)

def BufferLine(dsSrc, dtSrc, dsDst, dtDst, strUnit, strEndType, strR, iLeftSide, iUnion, iSegment, iRing):
            sm.BufferMulti(dsSrc, dtSrc, dsDst, dtDst, strUnit, strEndType, strR, 
                                    iLeftSide, iUnion, iSegment, iRing)


if __name__ == '__main__':
            bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#��oracle����Դ
            if bOpen == 1:
                        dtSrc = '����'
                        dtDst = '����buf'
                        strUnit = 'Meter'
                        sm.DeleteDataset(odsAlias, dtDst)
                        strDtType = sm.GetDatasetType(odsAlias, dtSrc)

                        if strDtType.lower()=='point' or strDtType.lower()=='region':
                                    print strDtType
                                    Buffer(odsAlias, dtSrc, odsAlias, dtDst, strUnit,
                                                            '30,45, 56', 0, 12, 1)
                        elif strDtType.lower()=='line':
                                    BufferLine(odsAlias, dtSrc, odsAlias, dtDst, strUnit,
                                                            'Flat', '30,45,56',1, 0,100, 1)
                        
                        sm.CloseDataSource(odsAlias)        
            else:
                        print "������Դʧ�ܣ�"
            sm.Exit()#�����������ͷ��ڴ�

