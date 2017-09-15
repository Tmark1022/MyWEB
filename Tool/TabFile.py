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
from Tool import ServerPrint

class TabFileEngine(object):
	def __init__(self):
		self.path_name = None
	
	def bind(self, path_name):
		if not os.path.isfile(path_name):
			ServerPrint.PrintWarning("TabFileEngine, bind绑定路径出现异常，路径不存在!")
			return
		self.path_name = path_name
	
	def split_config_line(self, line_str):
		split_list = line_str.split("	")
		if len(split_list) != 2:
			ServerPrint.print_warning("%s tabfile 配置文件的(%s)行内容格式不正确" % (self.path_name, line_str))
			return [None, None]
		return [split_list[0].strip(), split_list[1].strip()]
	
	def read_config(self):
		if not self.path_name:
			ServerPrint.PrintWarning("TabFileEngine, path_name没有绑定却要read_config读取操作!")
			return
		
		key_value_dict = {}
		with open(self.path_name,"r") as fd:
			# 判断文件头格式
			first_line = fd.readline()				# 第一行默认格式key[tab]value来识别文件格式
			first_line_split_list = self.split_config_line(first_line)
			if first_line_split_list[0] == None or first_line_split_list[0].lower() != "key" or first_line_split_list[1].lower() != "value":
				ServerPrint.PrintWarning("%s tabfile 配置文件的第一行不是key[tab]value形式")
				return key_value_dict
			
			# 读取文件配置，并加入到key_value_dict中
			for line_str in fd:
				line_list = self.split_config_line(line_str)
				if line_list[0] == None:
					continue
				if line_list[0] in key_value_dict:
					ServerPrint.PrintWarning("%s tabfile 配置文件存在相同的配置行(%s)" % (self.path_name, line_list[0]))
				key_value_dict[line_list[0]] = line_list[1]
		return key_value_dict

