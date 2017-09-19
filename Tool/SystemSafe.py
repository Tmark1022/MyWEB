#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-15
# module	: Tool.SystemSafe
#===================================================
import traceback
from Tool import ServerPrint

# 安全调用, 捕捉异常避免系统崩溃
def safe_call(func, *args, **kargs):
	try:
		return func(*args, **kargs)
	except Exception, e:
		traceback.print_exc()
		ServerPrint.PrintError(e)