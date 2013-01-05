"""
创建元数据库 
参数:
[in]string strServer 服务名; 
[in]string strUser 用户名; 
[in]string strPwd 密码; 
[in]string strEngType 引擎类型, 取值为: 
 ?sceOraclePlus
 ?sceSQLPlus 

返回:成功返回true. 

向元数据库批量导入元数据 
参数:
[in]string strServer 服务名; 
[in]string strUser 用户名; 
[in]string strPwd 密码; 
[in]string strEngType 引擎类型, 取值为: 
 ?sceOraclePlus
 ?sceSQLPlus 
[in]bool iDtNameChanged 是否转换数据集名称 
[in]string strPath 元数据所在路径 

返回:成功返回true. 

"""

# --*-- coding:cp936 --*--

import sys, os
sys.path.append(r'E:\Develop\UGO6.1\Builds\Win_Solution_vc9\BinD')
import smu as SuperMap

server='cp1'
user='dlgff'
pwd='dlgff'
engType='sceOraclePlus'
metaData=r'E:\工作\2012\2012-08\2012-08-02\MetadataImport\25meta\25meta'

#SuperMap.DropMetaDatabase(server, user, pwd, engType)
#SuperMap.CreateMetaDatabase(server, user, pwd, engType)
SuperMap.BatchImportMetaData(server, user, pwd, engType, 1, metaData)

