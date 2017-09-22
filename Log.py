#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-22
# module	: Log
#===================================================
import os
import logging
import logging.config
import Define.LogDefine
import Tool.SystemSafe
import Environment
import KV

__all__ = ["LogMessage"]

#====================================================
# 日志类型错误异常类
#====================================================
class LogTypeException(Exception):
	'''
	日志类型错误异常类
	'''
	def __init__(self, logger_flag):
		self.logger_flag = logger_flag
	
	def __str__(self):
		return "logger_flag(%s) not exist" % self.logger_flag

#====================================================
# 日志引擎类
#====================================================
class LogEngin(object):
	'''
	日志引擎类
	'''
	# 读取logging配置
	logging.config.fileConfig(Environment.ConfPath + os.sep + KV.get_value("log_config_file", "ha"))
	
	@classmethod
	@Tool.SystemSafe.safe_call_decorator
	def log_message(cls, logger_flag, message):
		if not isinstance(message, basestring):
			message = str(message)					# 如果不能转换为字符串形式，那么直接报错吧
		
		if logger_flag not in Define.LogDefine.LoggerRoute:
			raise LogTypeException(logger_flag)
		
		# logger_flag 为补位的话直接返回
		if logger_flag == Define.LogDefine.RootLogger:
			return
		
		# get logger
		logger_temp = logging.getLogger(Define.LogDefine.LoggerRoute[logger_flag])
		
		# log message
		log_func = LevelFuncRoute.get(logger_flag, cls._log_info)
		log_func(logger_temp, message)
	
	@classmethod
	def _log_error(cls, logger, message):
		logger.error(message)
	
	@classmethod
	def _log_warning(cls, logger, message):
		logger.warning(message)
		
	@classmethod
	def _log_info(cls, logger, message):
		logger.info(message)


# log等级函数路由, 有一些log需要不同的loggging log level 处理
LevelFuncRoute = {Define.LogDefine.ErrorLogger : LogEngin._log_error, 
				Define.LogDefine.WarningLogger : LogEngin._log_warning,
				}

LogMessage = LogEngin.log_message
