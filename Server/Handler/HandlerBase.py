#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-20
# module	: Server.Handler.HandlerBase
#===================================================
import tornado.web
from Server import Session

#====================================================
# BaseHandler基类
#====================================================
class BaseHandler(tornado.web.RequestHandler):
	handler_flag = None			# 用于标记是BaseHandler类继承链的标记
	
	def initialize(self):
		self.session = Session.Session(self.application.session_manager, self)			# 为每一个连接初始化一个session, redis中有的那么就读取redis中的数据，redis中没有的那么就创建一个空的
		
	def write_error(self, status_code, **kwargs):
		self.write("<h1>override write_error function</h1>")

	def __str__(self, *args, **kwargs):
		return "requestHandler派生类 对象: %s" % self.__class__.__name__
	
	def on_finish(self):
		# 不能在on_finish后调用self.session.save()， 因为响应已经返回，
		# 这时是不能设置set_secure_cookie的，只能将数据保存到数据库中
		# 必须要在返回前调用self.session.save()
		# self.session.save()
		
#		print "self.request.method = ", self.request.method
#		print "self.request.uri", self.request.uri
#		print "self.request.path", self.request.path
#		print "self.request.query", self.request.query
#		print "self.request.version", self.request.version
#		print "self.request.headers", self.request.headers
#		print "self.request.body", self.request.body
#		print "self.request.remote_ip", self.request.remote_ip
#		print "self.request.protocol", self.request.protocol
#		print "self.request.host", self.request.host
#		
#		print self.request
		pass
	
	# 保存session函数，不能定义为修饰体，因为不知道修饰的func是什么行为（会不会调用一些提前返回相应终止链接的行为）
	def save_session(self):
		self.session.save()