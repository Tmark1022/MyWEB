#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-19
# module	: Server.Handler.Index
#===================================================
from Server.Handler import HandlerBase
from Server import Application
from Tool import TimeMgr


#====================================================
# 主页handler
#====================================================
class IndexHandler(HandlerBase.BaseHandler):
	def get(self):
		self.session["times"] = (self.session["times"] + 1) if self.session.get("times") else 1
		self.session["last_time"] = TimeMgr.get_local_time()
		
		# 保存session
		self.save_session()
		self.write("<h1>这是一个主页。</h1>")
		self.write("<p>这是第 <b>%s</b> 次访问， 上一次访问时间<b>%s</b></p>" % (self.session["times"], self.session["last_time"]))


#class Error404Handler(HandlerBase.BaseHandler):
#	def get(self, path):
#		self.write("<h1>404 not found.</h1>")
#		self.write("%s 页面还没开发出来" % path)


# 避免reload的时候再次执行（现在还没实现reload，reload使得程序能够实时更新代码）
if __doc__ is not True:
	Application.Application.append_route((r"/", IndexHandler))
	#Application.Application.append_route((r"/(.*)", Error404Handler))