# --*-- coding: cp936 --*--
import os, sys, time
ugo=r'F:\Temp\2012-08-07\Bin'
sys.path.append(ugo)

import subprocess
import smu

def main(wkspc, map, dir, scidir):
	for root, dirs, files in os.walk(scidir):
		for file in files:
			if file[-4:len(file)].lower()=='.sci':
				sci = os.path.join(root, file)
				smu.BuildFromTaskFile(wkspc, map, dir, sci)


if __name__ == '__main__':
	if len(sys.argv)==5:
		wkspc = sys.argv[1] # 工作空间路径
		map = sys.argv[2]  # 地图名称
		dir = sys.argv[3] # 缓存生成目录
		time_s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		if os.path.isfile(sys.argv[4]):
			sci = sys.argv[4] # 缓存配置文件
			smu.BuildFromTaskFile(wkspc, map, dir, sci)
		elif os.path.isdir(sys.argv[4]):
			scidir = sys.argv[4]
			main(wkspc, map, dir, scidir)
		
		time_e = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		print time_s, time_e
