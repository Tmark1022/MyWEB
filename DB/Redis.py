#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-25
# module	: DB.Redis
#===================================================
import os
import redis
import Environment
from Tool import Serialize, TabFile

#====================================================
# 连接配置
#====================================================
# 默认配置或者配置表需包含以下东西等
ConnectConfig = { "host" : 'localhost', 
				"port" : 6379,
				"db" : 0,
				"password" : None}
# 读文件刷新配置
if os.path.isfile(Environment.ConfPath + os.sep + "Redis.conf"):
	TabFileObj = TabFile.TabFileEngine()
	TabFileObj.bind(Environment.ConfPath + os.sep + "Redis.conf")
	ConnectConfig.update(TabFileObj.read_config())
# 将配置表是字符串的改成数值
ConnectConfig["port"] = int(ConnectConfig["port"])
ConnectConfig["db"] = int(ConnectConfig["db"])

#====================================================
# redis数据库类
#====================================================
class RedisEngine(object):
	'''
	redis数据库连接操作管理类
	'''
	
	# 类变量定义 ConnectionPool
	pool = redis.ConnectionPool(**ConnectConfig)
	# 键名前缀,'cache-' + uuid.uuid4 + '-'
	key_prefix = "cache-40bd42dd-4982-45bc-82ad-e36ab4a2234d-"
	
	def __init__(self):
		self.db = self.connect()
	
	def connect(self):
		return redis.Redis(connection_pool = self.pool)

	def get(self, key):
		full_key = self.key_prefix + key
		pickle_value = self.db.get(full_key)
		# 已经过期了，就直接返回
		if pickle_value is None:
			return pickle_value
		return Serialize.str2obj(pickle_value)
	
	def set(self, key, value, expire_time = None):
		full_key = self.key_prefix + key
		# 将value序列化
		pickle_value = Serialize.obj2str(value)
		self.db.set(full_key, pickle_value, expire_time)

if __name__ == "__main__":
	obj = RedisEngine()
	# obj.set("haha", {"name" : "tmark", "age" : 22}, 10)
	print obj.get("haha")
