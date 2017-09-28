#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-25
# module	: DB.Mysql
#===================================================
import os
import MySQLdb
import Environment
from Tool import TabFile, ServerPrint, SystemSafe

#====================================================
# 连接配置
#====================================================
ConnectConfig = {}
# 读文件刷新配置
if os.path.isfile(Environment.ConfPath + os.sep + "Mysql.conf"):
	TabFileObj = TabFile.TabFileEngine()
	TabFileObj.bind(Environment.ConfPath + os.sep + "Mysql.conf")
	ConnectConfig.update(TabFileObj.read_config())

# 将配置表是字符串的改成数值
ConnectConfig["port"] = int(ConnectConfig["port"])

def get_connect_info():
	return ConnectConfig

#====================================================
# 数据库表字典
#====================================================
table_format = "create table %s (%s)"
TableDict = {"user" : table_format % ("user", "user_id varchar(20) not null primary key, passwd varchar(20) not null, nick_name varchar(20) not null"),
			
			}

#====================================================
# mysql 数据库管理类
#====================================================
class MysqlEngine(object):
	def __init__(self, host, port, user, passwd, db, charset = "utf8"):
		self.db = MySQLdb.connect(host = host,
								port = port,
								user = user,
								passwd = passwd,
								db = db,
								charset = charset)
		
		# self.db.cursorclass = MySQLdb.cursors.DictCursor			# 以（{}，{}）的形式返回
		
	def	__del__(self):
		'''
		对象释放的时候确保数据库连接断开
		'''
		if self.db is not None:
			self.db.close()
			self.db = None
	
	def check_and_create_table(self, table_dict):
		'''
		检查数据库表变更情况
		@param table_dict:
		'''
		cursor = self.db.cursor()
		temp_num = cursor.execute("show tables;")
		table_list = cursor.fetchmany(temp_num)
		for table_name in table_dict.keys():
			if (table_name,) not in table_list:
				cursor.execute(table_dict[table_name])
				# 输出创建新表的消息提示
				ServerPrint.PrintInfo(table_dict[table_name])
		
		# 判断数据表创建完成
		temp_num = cursor.execute("show tables;")
		table_list = cursor.fetchmany(temp_num)
		assert len(table_list) == len(table_dict), "数据表创建发生错误"
		
		cursor.close()
		self.db.commit()
	
	@SystemSafe.safe_call_decorator
	def run_sql(self, sql_str, debug = False):
		'''
		执行sql命令
		'''
		cursor = self.db.cursor()
		if debug:
			ServerPrint.PrintNormal("SQL : " + sql_str)
		temp_num = cursor.execute(sql_str)
		res_list = cursor.fetchmany(temp_num)
		cursor.close()
		self.db.commit()
		# 增、删、改都是返回空()
		return res_list
		
	
	'''
	sql 数据元素详解：
	sql_dict = {
		sql : string,  直接执行sql语句
		debug : (True or False), 执行sql命令前是否打印sql命令
		field : string, 生成select filed, 默认field 为 *
		table : string, 表名(每一种的数据库操作都需要包含)
		prerequisite : string, 生成 where prerequisite
		values : string, 生成value(....)
		set : string, 生成 set a = 10, b = 100等
		sort : order by user_id desc, select 的时候排序(select限定使用)
		limit : string, 分页查询(select限定使用)
	}
	'''
	def add_data(self, sql_dict):
		'''
		增加数据， insert命令
		'''
		if isinstance(sql_dict, basestring):
			sql_dict = {"sql" : sql_dict}
		if "sql" in sql_dict:
			return self.run_sql(sql_dict["sql"], sql_dict.get("debug", False))
		
		# sql_dict必须包含的字段判断
		if "table" not in sql_dict or "values" not in sql_dict:
			ServerPrint.PrintWarning("sql_dict不全包含table和values字段：%s" % sql_dict)
			return 
		
		# 开始构造sql命令
		table_name = sql_dict["table"]
		values = sql_dict["values"]
		sql_str = "INSERT INTO `%s` VALUES (%s)" % (table_name, values)
		return self.run_sql(sql_str, sql_dict.get("debug", False))
		
	def delete_data(self, sql_dict):
		'''
		删除数据， delete命令
		'''
		if isinstance(sql_dict, basestring):
			sql_dict = {"sql" : sql_dict}
		if "sql" in sql_dict:
			return self.run_sql(sql_dict["sql"], sql_dict.get("debug", False))
		
		# sql_dict必须包含的字段判断
		if "table" not in sql_dict:
			ServerPrint.PrintWarning("sql_dict不包含table字段：%s" % sql_dict)
			return 
		
		# 开始构造sql命令
		table_name = sql_dict["table"]
		prerequisite = sql_dict.get("prerequisite")
		
		sql_str = "DELETE FROM `%s` " % table_name
		if prerequisite is not None:
			prerequisite = " WHERE (%s)" % prerequisite
			sql_str = sql_str + prerequisite
			
		return self.run_sql(sql_str, sql_dict.get("debug", False))
	
	def query_data(self, sql_dict):
		'''
		查找数据
		'''
		if isinstance(sql_dict, basestring):
			sql_dict = {"sql" : sql_dict}
		if "sql" in sql_dict:
			return self.run_sql(sql_dict["sql"], sql_dict.get("debug", False))
		
		# sql_dict必须包含的字段判断
		if "table" not in sql_dict:
			ServerPrint.PrintWarning("sql_dict不包含table字段：%s" % sql_dict)
			return 
		
		# 开始构造sql命令
		table_name = sql_dict["table"]
		field_str = sql_dict.get("field", "*")
		prerequisite = " WHERE (%s) " % sql_dict.get("prerequisite","") if sql_dict.get("prerequisite","") else ""
		sort_str = sql_dict.get("sort", "")
		limit = "limit %s" % sql_dict.get("limit","") if sql_dict.get("limit","") else ""
		
		sql_str = "SELECT %s FROM `%s` %s %s %s" % (field_str, table_name, prerequisite, sort_str, limit)
			
		return self.run_sql(sql_str, sql_dict.get("debug", False))
	
	
	def modify_data(self, sql_dict):
		'''
		修改数据, update命令
		'''
		if isinstance(sql_dict, basestring):
			sql_dict = {"sql" : sql_dict}
		if "sql" in sql_dict:
			return self.run_sql(sql_dict["sql"], sql_dict.get("debug", False))
		
		# sql_dict必须包含的字段判断
		if "table" not in sql_dict or "set" not in sql_dict:
			ServerPrint.PrintWarning("sql_dict不全包含table和set字段：%s" % sql_dict)
			return 
		
		# 开始构造sql命令
		table_name = sql_dict["table"]
		set_str = sql_dict["set"]
		prerequisite = sql_dict.get("prerequisite")
		
		sql_str = "UPDATE `%s` SET %s " % (table_name, set_str)
		if prerequisite is not None:
			prerequisite = " WHERE (%s)" % prerequisite
			sql_str = sql_str + prerequisite
			
		return self.run_sql(sql_str, sql_dict.get("debug", False))
		
if __name__ == "__main__":
	db_obj = MysqlEngine(**get_connect_info())
	db_obj.check_and_create_table(TableDict)
	
	# print db_obj.run_sql("INSERT INTO `user` (`user_id`, `passwd`, `nick_name`) VALUES ('3', '2', '2')", True)
	# print db_obj.add_data({"values" : "'5', '1', '1'", "table" : "user", "debug" : True})
	# print db_obj.delete_data({"table" : "user", "debug" : True, "prerequisite" : "user_id = '2'"})
	# print db_obj.modify_data({"table" : "user", "debug" : True, "prerequisite" : "user_id = '2'", "set" : "passwd = '1000', nick_name = 'tmark'"})
	print db_obj.query_data({"table" : "user", "debug" : True, "field" : "user_id, nick_name", "sort" : "order by user_id desc", "limit" : "0,5"})
	