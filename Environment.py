#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-14
# module	: Environment
#===================================================
import os, sys
import platform

#====================================================
# 路径全局变量
#====================================================
RootPath = os.path.dirname(__file__)

#====================================================
# 将根目录加入sys.path
#====================================================
if RootPath not in sys.path:
	sys.path.append(RootPath)

#====================================================
# 获取当前操作系统平台
#====================================================
PlatForm = platform.system()		#Windows or Linux

def is_window():
	return PlatForm == "Windows"

def is_linux():
	return PlatForm == "Linux"

#====================================================
# config		读./Conf/MyWeb.conf
#====================================================



if __name__ == "__main__":
	print RootPath,PlatForm