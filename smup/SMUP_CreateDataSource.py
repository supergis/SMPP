# coding: GB2312
#===================================
#创建数据源
#CreateDataSource       
#===================================
import os
import sys
sys.path.append(r'..\..\Bin') #将组件的路径添加到环境变量
import smu as SuperMap #导入 SuperMap 模块

SuperMap.Init()#初始化 Python 组件环境;

#====================================
#需要修改的参数，以 UDBPlus 数据源为例
server=r"..\..\SampleData\Python\udbTest" 
user=""
password=""
alias="UDBPlus"
#====================================

isCreate=SuperMap.CreateDataSource(server,user,password,"sceUDB",alias)
if isCreate == 1:
    print "新建数据源成功。"
else:
    print "新建数据源失败！"
    
SuperMap.Exit()#清空组件环境释放内存
