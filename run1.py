#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 14:20
# @Author  : Zhangyp
# @File    : run.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from mssql import *
# from ReadConf import *
# import os
from shellcopy import *
import shutil
import decimal

PARA = conf() #  获取配置文件


def get_filepath():
	"""获取文件和路径dict"""
	ms = MSSQL(host=PARA['host'], user=PARA['user'], pwd=PARA['password'], db=PARA['dbname'])
	path = ms.ExecQuery(PARA['query_statement'])
	try:
		lp = []
		ln = []
		for i in range(len(path)):
			n = path[i][0].split('\\')[-1]
			ln.append(n)
			p = path[i][0].split(n)[0]
			p = p.split('\\',1)[1]
			lp.append(p)
		return ln, lp
	except Exception as e:
		logging.error(str(e))


def find_file():
	"""遍历file目录下所有文件"""
	try:
		cp = os.getcwd()
		f = [i for i in os.listdir(os.path.join(cp, 'file')) if not os.path.isdir(i)]
		return f
	except OSError as e:
		logging.error(str(e))
		return []


def generate_file(src_file, num):
	"""根据原文件生成指定数量的文件"""
	filepath = src_file.rpartition('\\')[0]+'\\'  # 提取路径
	filename = src_file.split('\\')[-1].split('.')[0]  # 提取文件名
	filesuffix = src_file.split('\\')[-1].split('.')[1]  # 提取后缀名
	for i in range(num):
		dst_file = filepath+filename+str(i)+'.'+filesuffix  # 新生成的文件
		shutil.copyfile(src_file, dst_file)

def main():
	"""将指定文件重命名，复制到指定文件夹"""
	(filename, paths) = get_filepath() # 获取目标文件的名字列表、相对路径
	try:
		abspath = [os.getcwd() + '\\newfile' + paths[i] for i in range(len(paths))]#  目标文件的绝对路径
		try:
			for i in range(len(abspath)):
				try:
					os.makedirs(abspath[i])# 创建目标文件路径
					logging.info('任务%s:文件夹->%s 创建成功' % (str(i), abspath[i]))
				except OSError as e:
					logging.error(str(e))
		except OSError as e:
			logging.warning(str(e))
		srcname = find_file()
		generate_file(os.getcwd()+'\\file\\'+srcname[0], len(filename)-1)
		srcnamelist = find_file()
		for i in range(len(srcnamelist)):
			'''重命名文件'''
			oldname = os.path.join(os.getcwd(), 'file', srcnamelist[i])  # 旧文件名
			newname = os.path.join(abspath[i], filename[i])  # 新文件名
			try:
				os.rename(oldname, newname)
				logging.info('任务%s:重命名文件%s' % (str(i), newname))
			except FileExistsError as e:
				logging.warning('%s【建议】清空newfile目录后重试'%str(e))
		if PARA['isshare'] == '1':
			openshare(PARA['path'], PARA['shareuser'], PARA['sharepwd'])
			shellcopy(os.getcwd() + '\\newfile', PARA['path'])
			closeshare()
		elif PARA['isshare'] == '0':
			mkdir(PARA['path'])
			shellcopy(os.getcwd() + '\\newfile', PARA['path'])
		else:
			pass
	except Exception as e:
		logging.info(str(e))
	
		
if __name__ == '__main__':
	main()
	# generate_file(r'E:\1\2ewrfewr.dcm', 2000)
	# print(find_file())
	