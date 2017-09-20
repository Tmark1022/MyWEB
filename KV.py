#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-20
# module	: KV
#===================================================
import os
import Environment
from Tool import TabFile

KVDict = {}

# 配置存在就使用config配置来更新KVDict
if os.path.isfile(Environment.ConfPath + os.sep + "KV.conf"):
	TabFileObj = TabFile.TabFileEngine()
	TabFileObj.bind(Environment.ConfPath + os.sep + "KV.conf")
	KVDict.update(TabFileObj.read_config())

#====================================================
# 对外访问接口
#====================================================
def get_value(key_name):
	return KVDict.get(key_name, None)