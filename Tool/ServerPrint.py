#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-14
# module	: Tool.ServerPrint
#===================================================
import Environment

#====================================================
# 系统打印模块
#====================================================
# 列表输出函数
def print_func(*args):
	for arg in args:
		# window 控制台中文默认编码GBK，真操蛋，这里默认输入的都是utf-8
		if Environment.is_window():
			print arg.decode("utf-8").encode("gbk"),
		else:
			print arg,


if Environment.is_window():										# window
	import ctypes
	
	STD_INPUT_HANDLE = -10
	STD_OUTPUT_HANDLE = -11
	STD_ERROR_HANDLE = -12
	
	# 字体颜色定义 ,关键在于颜色编码，由2位十六进制组成，分别取0~f，前一位指的是背景色，后一位指的是字体色
	# 由于该函数的限制，应该是只有这16种，可以前景色与背景色组合。也可以几种颜色通过或运算组合，组合后还是在这16种颜色中
	
	# Windows CMD命令行 字体颜色定义 text colors
	FOREGROUND_BLACK = 0x00 # black.
	FOREGROUND_DARKBLUE = 0x01 # dark blue.
	FOREGROUND_DARKGREEN = 0x02 # dark green.
	FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue.
	FOREGROUND_DARKRED = 0x04 # dark red.
	FOREGROUND_DARKPINK = 0x05 # dark pink.
	FOREGROUND_DARKYELLOW = 0x06 # dark yellow.
	FOREGROUND_DARKWHITE = 0x07 # dark white.
	FOREGROUND_DARKGRAY = 0x08 # dark gray.
	FOREGROUND_BLUE = 0x09 # blue.
	FOREGROUND_GREEN = 0x0a # green.
	FOREGROUND_SKYBLUE = 0x0b # skyblue.
	FOREGROUND_RED = 0x0c # red.
	FOREGROUND_PINK = 0x0d # pink.
	FOREGROUND_YELLOW = 0x0e # yellow.
	FOREGROUND_WHITE = 0x0f # white.
	
	# Windows CMD命令行 背景颜色定义 background colors
	BACKGROUND_BLUE = 0x10 # dark blue.
	BACKGROUND_GREEN = 0x20 # dark green.
	BACKGROUND_DARKSKYBLUE = 0x30 # dark skyblue.
	BACKGROUND_DARKRED = 0x40 # dark red.
	BACKGROUND_DARKPINK = 0x50 # dark pink.
	BACKGROUND_DARKYELLOW = 0x60 # dark yellow.
	BACKGROUND_DARKWHITE = 0x70 # dark white.
	BACKGROUND_DARKGRAY = 0x80 # dark gray.
	BACKGROUND_BLUE = 0x90 # blue.
	BACKGROUND_GREEN = 0xa0 # green.
	BACKGROUND_SKYBLUE = 0xb0 # skyblue.
	BACKGROUND_RED = 0xc0 # red.
	BACKGROUND_PINK = 0xd0 # pink.
	BACKGROUND_YELLOW = 0xe0 # yellow.
	BACKGROUND_WHITE = 0xf0 # white.
	
	# get handle
	std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
	
	def set_cmd_text_color(color, handle=std_out_handle):
		Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
		return Bool
	
	#reset white
	def resetColor():
		set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
	
	def decorate_print_top(fore_color, back_color = None):
		def decorate_print(func):
			def wrapper(*args, **kargs):
				if back_color == None:
					set_cmd_text_color(fore_color)
				else:
					set_cmd_text_color(fore_color | back_color)
				func(*args, **kargs)
				resetColor()
			return wrapper
		return decorate_print
	
	@decorate_print_top(FOREGROUND_RED)
	def print_error(*args):
		print "Error_Exc:",
		print_func(*args)
		print
	
	@decorate_print_top(FOREGROUND_YELLOW)
	def print_warning(*args):
		print "Warning_Exc:",
		print_func(*args)
		print
	
	@decorate_print_top(FOREGROUND_GREEN)
	def print_info(*args):
		print "Info:",
		print_func(*args)
		print
		
elif Environment.is_linux():								# linux
	'''
	-------------------------------------------
	字体色     |       背景色     |      颜色描述
	-------------------------------------------
	30        |        40       |       黑色
	31        |        41       |       红色
	32        |        42       |       绿色
	33        |        43       |       黃色
	34        |        44       |       蓝色
	35        |        45       |       紫红色
	36        |        46       |       青蓝色
	37        |        47       |       白色
	-------------------------------------------
	'''
	# 前景色
	FOREGROUND_BLACK 	= 30
	FOREGROUND_RED 		= 31
	FOREGROUND_GREEN 	= 32
	FOREGROUND_YELLOW 	= 33
	FOREGROUND_BLUE 	= 34
	FOREGROUND_FUCHSIA 	= 35
	FOREGROUND_CYAN 	= 36
	FOREGROUND_WHITE 	= 37
	
	# 背景色
	BACKGROUND_BLACK 	= 40
	BACKGROUND_RED 		= 41
	BACKGROUND_GREEN 	= 42
	BACKGROUND_YELLOW 	= 43
	BACKGROUND_BLUE 	= 44
	BACKGROUND_FUCHSIA 	= 45
	BACKGROUND_CYAN 	= 46
	BACKGROUND_WHITE 	= 47
	
	def reset_color():
		print "\033[0m"
	
	def set_color(fore_color, back_color = None):
		if back_color == None:
			str_temp = "\033[1;%sm" % fore_color
			print str_temp,
		else:
			str_temp = "\033[1;%s;%sm" % (fore_color, back_color)
			print str_temp,
			
	def decorate_print_top(fore_color, back_color = None):
		def decorate_print(func):
			def wrapper(*args, **kargs):
				set_color(fore_color, back_color)
				func(*args, **kargs)
				reset_color()
			return wrapper
		return decorate_print
	
	
	@decorate_print_top(FOREGROUND_RED)
	def print_error(*args):
		print "Error_Exc:",
		print_func(*args)
	
	@decorate_print_top(FOREGROUND_YELLOW)
	def print_warning(*args):
		print "Warning_Exc:",
		print_func(*args)
	
	@decorate_print_top(FOREGROUND_GREEN)
	def print_info(*args):
		print "Info:",
		print_func(*args)

else:														# other
	def print_error(*args):
		print "Error_Exc:",
		print_func(*args)
		print
	
	def print_warning(*args):
		print "Warning_Exc:",
		print_func(*args)
		print
	
	def print_info(*args):
		print "Info:",
		print_func(*args)
		print
	
#====================================================
# 汇总接口
#====================================================
__all__ = ["PrintError", "PrintWarning", "PrintInfo"]

PrintError = print_error
PrintWarning = print_warning
PrintInfo = print_info
