#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-27
# module	: Tool.Serialize
#===================================================
#====================================================
# pickle
#====================================================
try:
	import cPickle as pickle
except ImportError:
	import pickle

def obj2str(obj_temp):
	return pickle.dumps(obj_temp)

def str2obj(str_temp):
	return pickle.loads(str_temp)

#====================================================
# json
#====================================================
import json

def obj2json(obj_temp):
	return json.dumps(obj_temp)

def json2obj(str_temp):
	return json.loads(str_temp)

if __name__ == "__main__":
	obj = {"name" : "tmark", "age" : 22, "phone" : "123456789"}
	str_pickle = obj2str(obj)
	print str_pickle
	print str2obj(str_pickle)
	
	str_json = obj2json(obj)
	print str_json
	print json2obj(str_json)