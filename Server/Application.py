#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-19
# module	: Server.Application
#===================================================
import tornado.web
import Environment
import KV
from Tool import LoadModule,ServerPrint
from Server import Session

#====================================================
# Application应用类
#====================================================
class Application(tornado.web.Application):
	handlers = []
	
	def __init__(self):
		settings = {
				"cookie_secret" 	: KV.get_value("cookie_secret", "MyWeb_cookie_secret"),
				"session_secret"	: KV.get_value("session_secret", "MyWeb_session_secret"),
				"session_timeout"	: KV.get_value("session_timeout", 60),
				
				}
		tornado.web.Application.__init__(self, handlers=self.handlers, **settings)
		self.session_manager = Session.SessionManager(settings["session_secret"], settings["session_timeout"])
		
#		settings = dict(
#            cookie_secret = "e446976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f==78d",
#            session_secret = "3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
#            session_timeout = 60,
#            template_path = os.path.join(os.path.dirname(__file__), "templates"),
#            static_path = os.path.join(os.path.dirname(__file__), "static"),
#            xsrf_cookies = True,
#            login_url = "/login",
#        )



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



