#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-15
# module	: Start
#===================================================
import os, sys
#====================================================
# 最先的操作将根目录加入sys.path
#====================================================
RootPath_temp = os.path.dirname(__file__)
if RootPath_temp not in sys.path:
	sys.path.append(RootPath_temp)
	
#====================================================
# 主要逻辑从这里开始
#====================================================
from Server import ParseCmd
import Server.Application
import tornado.ioloop


# 这个函数执行到最后边就会进入ioloop了， 所以这个函数要放在最后边哦
def tornado_start():
	Server.Application.load_all_handlers()
	app = Server.Application.make_app()
	app.listen(1234)
	tornado.ioloop.IOLoop.instance().start()
	
def main():
	# 命令行解析
	options, _ = ParseCmd.parse_cmd_line()
	for _option, _value in options:
		if _option == "--help":
			ParseCmd.help_info()
			return
	
	# 开启tornado web 服务
	tornado_start()

if __name__ == "__main__":
	main()
