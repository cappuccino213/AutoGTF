#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 11:18
# @Author  : Zhangyp
# @File    : mssql.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import pymssql
from ReadConf import *


class MSSQL:
	"""
	对pymssql的简单封装
	使用该库时，需要在Sql Server configuration Mnanage里面将TCP/IP协议开启
	"""
	
	def __init__(self, host, user, pwd, db):
		self.host = host
		self.user = user
		self.pwd = pwd
		self.db = db
		
	
	def __GetConnect(self):
		if not self.db:
			raise (NameError, "没有设置数据库信息")
		self.conn = pymssql.connect(host=self.host,
									user=self.user,
									password=self.pwd,
									database=self.db
									)
		cur = self.conn.cursor()
		if not cur:
			raise (NameError, "连接数据库失败")
		else:
			return cur
		
	
	def ExecQuery(self, sql):
		cur = self.__GetConnect()
		try:
			cur.execute(sql)
			resList = cur.fetchall()
			return resList
		except Exception as ex:
			logging.warning(str(ex))
		finally:
			self.conn.close()
			
	
	def ExecNoQuery(self, sql):  # 更新语句
		cur = self.__GetConnect()
		try:
			cur.execute(sql)
			self.conn.commit()
		except Exception as ex:
			logging.warning(str(ex))
			self.conn.rollback()
		finally:
			self.conn.close()
			
	
	def ExecMany(self, sql, list):  # 更新语句
		cur = self.__GetConnect()
		try:
			cur.executemany(sql, list)
			self.conn.commit()
		except Exception as ex:
			logging.warning(str(ex))
			self.conn.rollback()
		finally:
			self.conn.close()


# if __name__ == '__main__':
# 	L = conf()
# 	# print(L['host'],L['query_statement'])
# 	ms = MSSQL(host = L['host'], user = L['user'], pwd=L['password'], db = L['dbname'])
# 	path = ms.ExecQuery(L['query_statement'])
# 	print(type(path),path)