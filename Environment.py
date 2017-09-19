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
ConfPath = RootPath + os.sep + "Conf"
ToolPath = RootPath + os.sep + "Tool"

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

#====================================================
# config		读./Conf/MyWeb.conf
#====================================================
from Tool import TabFile										# 依赖于上边的PlatForm， 所以不能放在获取当前操作系统平台操作之前

KVDict = {}

# 配置存在就使用config配置来更新KVDict
if os.path.isfile(ConfPath + os.sep + "MyWeb.conf"):
	TabFileObj = TabFile.TabFileEngine()
	TabFileObj.bind(ConfPath + os.sep + "MyWeb.conf")
	KVDict.update(TabFileObj.read_config())

def get_value(key_name):
	return KVDict.get(key_name, None)



if __name__ == "__main__":
	print RootPath,PlatForm, ConfPath, ToolPath