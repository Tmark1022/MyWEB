#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-19
# module	: Server.Application
#===================================================
import tornado.web
import Environment
from Tool import LoadModule,ServerPrint

#====================================================
# Application应用类
#====================================================
class Application(tornado.web.Application):
	handlers = []
	
	def __init__(self):
		settings = {}
		tornado.web.Application.__init__(self, handlers=self.handlers, **settings)
		
	@classmethod
	def append_route(cls, route_tuple):
		if not isinstance(route_tuple[0], basestring):
			ServerPrint.PrintWarning("append_route 中 route_tuple(%s, %s)格式异常" % (route_tuple[0], route_tuple[1]))
			return
		if not hasattr(route_tuple[1], "handler_flag"):
			ServerPrint.PrintWarning("append_route 中 route_tuple(%s, %s)格式异常，Handler处理类不是BaseHandler类的子类" % (route_tuple[0], route_tuple[1]))
			return
		if route_tuple in cls.handlers:
			ServerPrint.PrintWarning("append_route 中 route_tuple(%s, %s)重复append" % (route_tuple[0], route_tuple[1]))
			return
		cls.handlers.append(route_tuple)
	
	@classmethod
	def remove_route(cls, route_tuple):
		if route_tuple not in cls.handlers:
			return
		cls.handlers.remove(route_tuple)
		
# 注意先要调用load_all_handlers来构造handlers再调用这个函数来产生Application对象
def make_app():
	print Application.handlers
	return Application()

#====================================================
# 导入所有handler处理类，并构造handlers列表（为了避免import循环有可能导致一些列傻逼问题，这里定义为函数直接让这个模块导入完成）
#====================================================
# 这个函数其实可以设置为直接执行的语句也没问题，因为Handler里边的模块是调用Application类，
# 就算Application模块没有导入完成，但是Application.Application 已经是可以使用了，
# 所以这个时候import循环也不会出现问题（python是可以循环import的，但是需要注意其import顺序就行）
def load_all_handlers():
	module_names = LoadModule.get_all_module(Environment.HandlerPath)
	LoadModule.add_prefix(module_names, "Server.Handler.")
	LoadModule.load_modules(module_names)



