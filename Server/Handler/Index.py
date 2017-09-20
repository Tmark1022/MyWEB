#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-19
# module	: Server.Handler.Index
#===================================================
from Server.Handler import HandlerBase
from Server import Application

#====================================================
# 主页handler
#====================================================
class IndexHandler(HandlerBase.BaseHandler):
	def get(self):
		self.write("<h1>这是一个主页。</h1>")


class NameHandler(HandlerBase.BaseHandler):
	def get(self):
		self.write("<h1>i am tmark。</h1>")


# 避免reload的时候再次执行（现在还没实现reload，reload使得程序能够实时更新代码）
if __doc__ is not True:
	Application.Application.append_route((r"/", IndexHandler))
	Application.Application.append_route((r"/name", NameHandler))