#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-14
# module	: Environment
#===================================================
import os
import platform

#====================================================
# 路径全局变量
#====================================================
RootPath 	= os.path.dirname(__file__)
ConfPath 	= RootPath + os.sep + "Conf"
ToolPath 	= RootPath + os.sep + "Tool"
ServerPath 	= RootPath + os.sep + "Server"
HandlerPath	= ServerPath + os.sep + "Handler"

#====================================================
# 将根目录加入sys.path, 在Start模块加入了
#====================================================
#if RootPath not in sys.path:
#	sys.path.append(RootPath)

#====================================================
# 获取当前操作系统平台
#====================================================
PlatForm = platform.system()		#Windows or Linux

def is_window():
	return PlatForm == "Windows"

def is_linux():
	return PlatForm == "Linux"



if __name__ == "__main__":
	print RootPath,PlatForm, ConfPath, ToolPath