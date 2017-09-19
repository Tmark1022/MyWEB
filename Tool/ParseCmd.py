#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-19
# module	: Tool.ParseCmd
#===================================================
import getopt
import sys
from Tool import SystemSafe

#====================================================
# 解析命令行参数接口
#====================================================
def parse_cmd_line(args = sys.argv[1:], shortopts = "c:", longopts = ["help"]):
	return SystemSafe.safe_call(getopt.getopt, args, shortopts, longopts)