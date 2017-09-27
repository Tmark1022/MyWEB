#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-20
# module	: Server.Handler.HandlerBase
#===================================================
import tornado.web

#====================================================
# BaseHandler基类
#====================================================
class BaseHandler(tornado.web.RequestHandler):
	handler_flag = None			# 用于标记是BaseHandler类继承链的标记
	
	def write_error(self, status_code, **kwargs):
		self.write("<h1>override write_error function</h1>")

	def __str__(self, *args, **kwargs):
		return "requestHandler派生类 对象: %s" % self.__class__.__name__
	
	def on_finish(self):
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