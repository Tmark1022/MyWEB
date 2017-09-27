#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-25
# module	: DB.Redis
#===================================================
import redis


pool = redis.ConnectionPool(host = "127.0.0.1", port = 6379, db = 0)				# connect pool 的 作用就是对个strictredis实例共享一个连接， connect pool能使断线重连

r = redis.Redis(connection_pool = pool)
r.set("name", "tmark")
print r.get("name")


#====================================================
# 连接配置
#====================================================
# 默认配置或者配置表需包含以下东西等
#host='localhost', 
#port=6379,
#db=0
#password=None,

# 获得redis连接配置函数，使用到tabfile获取配置
def get_redis_file_connect_config(file_name):
	pass


#====================================================
# redis数据库类
#====================================================
class RedisEngine(object):
	'''
	info
	'''
	
	# 类变量定义 ConnectionPool
	# pool = redis.ConnectionPool(host = "127.0.0.1", port = 6379, db = 0)o
	
	
	def __init__(self, file_name = None):
		self.db = self.connect()
	
	def connect(self):
#		return redis对象
		pass
	
	
	# 只对字符串操作， 将python对象pickle序列在存储等
	def get(self, key):
		pass
	
	def set(self, key, value):
		pass




#====================================================
# 需要编写加密和序列化模块
#====================================================



