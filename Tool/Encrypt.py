#-*- coding:UTF-8 -*-
#===================================================
# author	: Tmark
# date 		: 2017-9-27
# module	: Tool.Encrypt
#===================================================
import hashlib
import base64
import uuid
import KV

#====================================================
# 加密模块
#====================================================
# md5 加密
def md5(encrypt_str):
	# 默认转换为字符串
	if not isinstance(encrypt_str, basestring):
		encrypt_str = str(encrypt_str)
	salt = KV.get_value("salt", "MyWeb")
	m = hashlib.md5()
	m.update(encrypt_str + salt)
	return m.hexdigest()

# sha1 加密
def sha1(encrypt_str):
	# 默认转换为字符串
	if not isinstance(encrypt_str, basestring):
		encrypt_str = str(encrypt_str)
	salt = KV.get_value("salt", "MyWeb")
	s = hashlib.sha1()
	s.update(encrypt_str + salt)
	return s.hexdigest()

# 清除base64编码的尾部补充字符 "="
def del_equal(str_temp):
	# 最多补充的"="是两个
	res_str = str_temp
	# 第一次
	if res_str[-1] == "=":
		res_str = res_str[:-1]
	else:
		return res_str
	
	# 第二次
	if res_str[-1] == "=":
		res_str = res_str[:-1]
	
	return res_str
		
# 补上base64编码的尾部补充字符 "="
def add_equal(str_temp):
	# str_temp 需要是
	add_num = len(str_temp) % 4
	res_str = str_temp + add_num * "="
	return res_str

# base64 加密
def base64_encode(encode_str):
	# 默认转换为字符串
	if not isinstance(encode_str, basestring):
		encode_str = str(encode_str)
	
	return del_equal(base64.b64encode(encode_str))

# base64 解码
def base64_decode(decode_str):
	if not isinstance(decode_str, basestring):
		decode_str = str(decode_str)
	decode_str = add_equal(decode_str)
	return base64.b64decode(decode_str)

# url_base64 加密
def url_base64_encode(encode_str):
	# 默认转换为字符串
	if not isinstance(encode_str, basestring):
		encode_str = str(encode_str)
	
	return del_equal(base64.urlsafe_b64encode(encode_str))

# url_base64 解码
def url_base64_decode(decode_str):
	if not isinstance(decode_str, basestring):
		decode_str = str(decode_str)
	decode_str = add_equal(decode_str)
	return base64.urlsafe_b64decode(decode_str)

#====================================================
# 生成随机数
#====================================================
def uuid_random():
	return uuid.uuid4()


if __name__ == "__main__":
#	print uuid_random()
#	print md5("i am so handsome")
#	print sha1("i am so handsome")
#	temp_base64 = base64_encode("i\xb7\x1d\xfb\xef\xff")
#	print temp_base64
#	print base64_decode(temp_base64)
#	temp_base64 = url_base64_encode("i\xb7\x1d\xfb\xef\xff")
#	print temp_base64
#	print url_base64_decode(temp_base64)
	print base64_encode(uuid_random().bytes + uuid_random().bytes)

