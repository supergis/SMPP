"""
创建金字塔 
参数:


[in]

string

strDsAlias 数据源别名; 



[in]

string

strDtName 数据集名称; 

返回:成功返回true. 
"""

# coding: GB2312

#===================================
import os
import sys
#====================================

def help():
            strhelp='''
创建金字塔
1. udb数据源
BuildPyramid.py [Bin] [udb] [dtName]

2. oracle数据源
BuildPyramid.py [Bin] [server] [user] [pwd] [dtName]

3. dtName为空时, 将对第一个数据集创建金字塔
            '''
            return strhelp

def main(server, user, pwd, engtype, dtName):
            odsAlias="oracle"
            bOpen=smu.OpenDataSource(server,user, pwd, engtype,odsAlias)
            if bOpen == 1:
                        if dtName=="''":
                                    dtName=smu.GetDatasetName(odsAlias, 0)
                        bBuild=smu.BuildPyramid(odsAlias,dtName)#创建影像金字塔
                        if bBuild == 1:
                                    print "创建金字塔成功"
                        else:
                                    print "创建影像金字塔失败！"
                        smu.CloseDataSource(odsAlias)
            else:
                        print "打开数据源失败！"
            
            smu.Exit()#清空组件环境释放内存

def udb(server, dtName):
            main(server, '', '', 'sceUDB', dtName)

def oracle(server, user, pwd, dtName):
            main(server, user, pwd, 'sceOraclePlus', dtName)


if __name__=='__main__':
            if len(sys.argv) >= 4:
                        ugo = sys.argv[1]
                        sys.path.append(ugo) #将.net组件的路径添加到环境变量
                        import smu
            else:
                        print help()
                        sys.exit()

            print len(sys.argv), sys.argv
            if len(sys.argv)==4:
                        server=sys.argv[2]
                        dtname=sys.argv[3]
                        udb(server, dtname)
            elif len(sys.argv)==6:
                        server=sys.argv[2]
                        user=sys.argv[3]
                        pwd=sys.argv[4]
                        dtname=sys.argv[5]
                        oracle(server, user, pwd, dtname)
