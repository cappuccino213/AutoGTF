#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 11:17
# @Author  : Zhangyp
# @File    : ReadConf.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import configparser
import logging
import datetime,os

dt = datetime.datetime.now()
logging.basicConfig(level = logging.DEBUG, filename = r'%s\log\%s.log'%(os.getcwd(),dt.strftime("%Y%m%d%H%M%S")), format = ('''[时间]:%(asctime)s
[线程]:%(thread)s
[级别]:%(levelname)s
[路径]:%(pathname)s
[函数]:%(funcName)s
[行号]:%(lineno)d
[信息]:%(message)s
------------------
'''))
#日志启用开关,注释掉即开启日志
# logging.disable(logging.DEBUG)

def conf():
	# 处理BOM字符（当配置文件被记事本编辑过后，会插入一个bom头）
	try:
		BOM = b'\xef\xbb\xbf'
		with open('config.ini', 'r+b') as f:
			if BOM == f.read(3):
				content = f.read()
				f.seek(0)
				f.write(content)
				f.truncate()
	except (FileNotFoundError,FileExistsError) as e:
		logging.info(str(e))
	try:
		cf = configparser.ConfigParser()
		cf.read('config.ini', encoding='utf-8')
		s = {}
		section = cf.sections()
		for i in range(len(section)):
			kv = cf.items(section[i])
			for j in range(len(kv)):
				s[kv[j][0]] = kv[j][1]
		return s
	except Exception as e:
		logging.error(str(e))
		
# if __name__ == '__main__':
# 	print(conf())
