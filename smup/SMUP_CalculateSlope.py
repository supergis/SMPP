# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster    
#===================================

"""
�¶ȼ���

����:
[in]string strDataSourceSrc Դ����Դ����; 
[in]string strDatasetGrid �������¶ȵ�դ�����ݼ�; 
[in]int iSlopeType �¶ȵĵ�λ����; 
 ?1 Degree�ԽǶ�Ϊ��λ����ʾ�¶�,
 ?2 Radian�Ի���Ϊ��λ����ʾ�¶�,
 ?3 Percent�԰ٷ�������ʾ�¶�, 
[in]double zFactor �߳�����ϵ��; 
[in]string strDataSourceDst �������Դ����; 
[in]string strDatasetName ������ݼ�������; 

����:�ɹ�����true. 
"""

import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·����ӵ���������
import smu as SuperMap #����SuperMapģ��

SuperMap.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\Temp\2012-08-25\�������.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
            bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#��oracle����Դ
            if bOpen == 1:
                        dtGrid = 'Dem2'
                        x1=726628.410093674
                        y1=3140482.5278305
                        z1=2953
                        SuperMap.DeleteDataset(odsAlias, 'dem22')
                        SuperMap.CalculateSlope(odsAlias, dtGrid, 1,1,odsAlias, 'dem22')
                        SuperMap.CloseDataSource(odsAlias)  
            else:
                        print "������Դʧ�ܣ�"
            SuperMap.Exit()#�����������ͷ��ڴ�
