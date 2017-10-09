#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-10-9
# module	: Tool.TimeMgr
#===================================================
import time

def get_local_time(t = None, time_format = "%a %H:%M:%S %Y-%m-%d"):
	try:
		if t is None:
			t = time.localtime()
		return time.strftime(time_format, t)
	except:
		return None