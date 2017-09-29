#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-29
# module	: Server.Session
#===================================================

#====================================================
# session支持，摘自github tornado-memcached-sessions项目
# 并根据我本身项目做相应的修改（使用我本身实现的一些模块，memacahe改redis等）
#====================================================
import hmac
import uuid
import hashlib
from DB import Redis


class SessionData(dict):
	def __init__(self, session_id, hmac_key):
		self.session_id = session_id
		self.hmac_key = hmac_key

class Session(SessionData):
	def __init__(self, session_manager, request_handler):
		self.session_manager = session_manager
		self.request_handler = request_handler			# 使用来自操作cookie的
		try:
			current_session = session_manager.get(request_handler)		# 从redis中获得SessionData对象
		except InvalidSessionException:
			# 如果连接的session_id被恶意篡改了，那么就创建一个空的session
			current_session = session_manager.get()
		
		# 构造数据
		for key, data in current_session.iteritems():
			self[key] = data
		
		self.session_id = current_session.session_id
		self.hmac_key = current_session.hmac_key

	def save(self):
		self.session_manager.set(self.request_handler, self)

class SessionManager(object):
	def __init__(self, secret, session_timeout):
		self.secret = secret
		self.session_timeout = session_timeout

	def _fetch(self, session_id):
		try:
			redis_obj = Redis.RedisEngine()
			session_data = redis_obj.get(session_id)		# 获得数据并且反序列化了
			# 数据库中的数据还没有过期
			if session_data != None:
				# 重新设置过期时间
				redis_obj.set(session_id, session_data, self.session_timeout)
				
			if type(session_data) == type({}):
				return session_data
			else:
				return {}
		except IOError:
			return {}
	
	# 获得数据
	def get(self, request_handler = None):
		if (request_handler == None):
			session_id = None
			hmac_key = None
		else:
			session_id = request_handler.get_secure_cookie("session_id")				# sha256加密了的session_id
			hmac_key = request_handler.get_secure_cookie("verification")				# 用来校验session_id 是否被篡改了
		
		if session_id == None:
			session_exists = False
			session_id = self._generate_id()
			hmac_key = self._generate_hmac(session_id)
		else:
			session_exists = True
		
		# 判断是否被篡改了
		check_hmac = self._generate_hmac(session_id)
		if hmac_key != check_hmac:
			raise InvalidSessionException()
		
		# 创建一个sessionData对象用于承载数据库中的数据并且返回
		session = SessionData(session_id, hmac_key)
		# 是否在数据库中保留数据
		if session_exists:
			session_data = self._fetch(session_id)
			for key, data in session_data.iteritems():
				session[key] = data
		return session

	# 保存数据
	def set(self, request_handler, session):
		request_handler.set_secure_cookie("session_id", session.session_id)
		request_handler.set_secure_cookie("verification", session.hmac_key)
		
		redis_obj = Redis.RedisEngine()
		redis_obj.set(session.session_id, dict(session.items()), self.session_timeout)

	def _generate_id(self):
		new_id = hashlib.sha256(self.secret + str(uuid.uuid4()))
		return new_id.hexdigest()

	def _generate_hmac(self, session_id):
		return hmac.new(session_id, self.secret, hashlib.sha256).hexdigest()

class InvalidSessionException(Exception):
	pass