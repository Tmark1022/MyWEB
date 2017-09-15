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
from Tool import TabFile


def main():
	tab_file_engin = TabFile.TabFileEngine()
	tab_file_engin.bind(r"./conf/MyWeb.conf")
	key_value_dict = tab_file_engin.read_config()
	import pprint
	pprint.pprint(key_value_dict)
	

if __name__ == "__main__":
	main()