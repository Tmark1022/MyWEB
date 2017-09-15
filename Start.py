#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-15
# module	: Start
#===================================================
import os, sys
#====================================================
# 最先的操作将根目录加入sys.path
#====================================================
RootPath_temp = os.path.dirname(__file__)
if RootPath_temp not in sys.path:
	sys.path.append(RootPath_temp)
	
	
#====================================================
# 主要逻辑从这里开始
#====================================================
from Tool.ServerPrint import *
import Environment














if __name__ == "__main__":
	PrintError("i am a error", "hahah")
	PrintWarning("i am a Warning", "memeda")
	PrintInfo("i am aa info")