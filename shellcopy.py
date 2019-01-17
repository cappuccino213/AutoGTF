#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 9:42
# @Author  : Zhangyp
# @File    : shellcopy.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from ReadConf import *
# import os


def openshare(path, pwd, user):
	"""创建共享路径"""
	try:
		cmd = 'net use H: %s %s/%s' % (path, pwd, user)
		logging.info('%s' % cmd)
		os.popen(cmd)
	except OSError as e:
		logging.error(str(e))


def closeshare():
	"""删除磁盘映射"""
	try:
		cmd = 'net use H: /D'
		logging.info('%s'%cmd)
		os.popen(cmd)
	except OSError as e:
		logging.error(str(e))


def shellcopy(srcfolder, dstfolder):
	"""复制文件夹"""
	try:
		cmd = 'xcopy %s %s /e /y' % (srcfolder, dstfolder)
		logging.info('%s' % cmd)
		os.popen(cmd)
	except OSError as e:
		logging.warning(str(e))

		
def mkdir(dstfolder):
	"""创建文件夹"""
	try:
		cmd = 'mkdir %s'%dstfolder
		logging.info('%s' % cmd)
		os.popen(cmd)
	except OSError as e:
		logging.warning(str(e))
		

def shelldelete(srcfolder):
	"""删除文件夹"""
	try:
		cmd = 'rmdir /s/q %s'%srcfolder
		logging.info('%s' % cmd)
		os.popen(cmd)
	except OSError as e:
		logging.error(str(e))

		
# if __name__ == '__main__':
# 	para = conf()
# 	if para['isshare'] == '1':
# 		openshare(para['path'], para['shareuser'], para['sharepwd'])
# 		shellcopy(r'E:\python\test_auto\AutoGTF\newfile',r'\\192.168.1.19\交换目录\zyp\share')
# 		closeshare()
# 		# shelldelete(r'E:\python\test_auto\AutoGTF\newfile')
# 	elif para['isshare'] == '0':
# 		shellcopy(r'E:\python\test_auto\AutoGTF\newfile', r'E:\python\test_auto\AutoGTF\newfile1')
# 	else:
# 		pass
	
	# print(para['isshare'],type(para['isshare']))