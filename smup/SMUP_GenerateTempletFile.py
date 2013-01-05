# --*-- coding: cp936 --*--
import os, sys
ugo=r'E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD'
sys.path.append(ugo)

import smu

def main(wkspc, map, sci, dir, iPicNum):
	smu.GenerateTempletFile(wkspc, map, sci, dir, iPicNum)


if __name__ == '__main__':
	if len(sys.argv)==6:
		wkspc = sys.argv[1]
		map = sys.argv[2]
		sci = sys.argv[3]
		dir = sys.argv[4]
		iPicNum = int(sys.argv[5])
		main(wkspc, map, sci, dir, iPicNum)
