#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-19
# module	: Tool.LoadModule
#===================================================
import os
import sys
import traceback

def get_all_module(root_floder, suffixs = ["py", "pyc", "pyo"]):
	'''
	@param root_floder:根目录
	@param suffixs:文件后缀
	@return: 模块名的集合
	'''
	# 修正suffixs查找
	if not isinstance(suffixs, set):
		suffixs = set(suffixs)
	# 非模块名路径长度
	unmodule_name_path_len = len(root_floder)
	# 结果集
	result = set()
	# 遍历所有的文件信息
	for dirpath, _, filenames in os.walk(root_floder):
		# 遍历所有的文件
		for fi in filenames:
			# __init__文件，导入包
			if fi == "__init__.py":
				fpns = dirpath
			# 构造文件路径
			else:
				fp = dirpath + os.sep + fi
				# 解析文件后缀
				pos = fp.rfind('.')
				if pos == -1:
					continue
				fpns, su = fp[:pos], fp[pos + 1:]
				# 不是模块文件，忽视之
				if su not in suffixs:
					continue
			# 将无后缀的文件路径变化为模块名
			module_name_temp = fpns[unmodule_name_path_len:]
			if module_name_temp.startswith(os.sep):
				module_name_temp = module_name_temp[1:]
			module_name = module_name_temp.replace(os.sep, '.')
			# 加入结果集
			if module_name: result.add(module_name)
	# 按模块名排序
	result = list(result)
	result.sort()
	return result

def load_modules(module_names):
	'''
	预导入模块，并设置标识位
	@param module_names:模块名集合
	'''
	SM = sys.modules
	for module_name in module_names:
		try:
			# 导入模块
			__import__(module_name)
			# 获取模块对象
			module = SM[module_name]
			# 标记该模块被预导入
			setattr(module, "__doc__", True)
		except :
			traceback.print_exc()

def add_prefix(module_names, prefix):
	list_len = len(module_names)
	for i in range(list_len):
		# 如果module_names里边的元素不是字符串，那就让其有问题输出出错信息吧
		module_names[i] = prefix + module_names[i]
	
if __name__ == "__main__":
	import Environment
	module_names = get_all_module(Environment.RootPath)
	print module_names
	load_modules(module_names)
	