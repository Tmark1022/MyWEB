#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-19
# module	: Server.ParseCmd
#===================================================
import getopt
import sys
from Tool import SystemSafe
from Define import NormalDefine

#====================================================
# 解析命令行参数接口
#====================================================
def parse_cmd_line(args = sys.argv[1:], shortopts = "", longopts = ["help"]):
	return SystemSafe.safe_call(getopt.getopt, args, shortopts, longopts)

#====================================================
# help帮助信息输出
#====================================================
def help_info():
	if not hasattr(NormalDefine, "HelpInfo"):
		print "Not help infomation."
	else:
		print NormalDefine.HelpInfo