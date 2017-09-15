#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-14
# module	: Tool.TabFile
#===================================================
#====================================================
# 读取以tab分割的key-value配置文件
#====================================================
import os


class TabFileEngine(object):
	def __init__(self):
		self.path_name = None
	
	def bind(self, path_name):
		if not os.path.isfile(path_name):
			pass