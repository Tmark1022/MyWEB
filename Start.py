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
import Environment
from Server import ParseCmd
from Tool import ServerPrint
from Define import NormalDefine


def main():
	# 命令行解析
	options, _ = ParseCmd.parse_cmd_line()
	for _option, _value in options:
		if _option == "--help":
			ParseCmd.help_info()
			return
	
	#....
	
	
	
if __name__ == "__main__":
	main()
