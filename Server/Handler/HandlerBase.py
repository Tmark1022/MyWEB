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