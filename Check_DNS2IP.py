# -*- coding: utf-8 -*- 
import socket
import time
from loguru import logger


def open_file(filename):
	file_data=[]
	try:
		with open(filename,encoding='utf-8') as f:
			for line in f:
				line=line.strip()
				s=line.split(':')
				file_data.append(s)
	except ZeroDivisionError:
		logger.exception(file_name+" - 文件读取出错！")
	else:
		pass
	finally:
		f.close()
	return file_data

def getIP(domainIP):
	for i in domainIP:
		j = i[0].split('|')
		domain = j[0]
		ip = j[1]
		try:
			myaddr1 = socket.getaddrinfo(domain, 'http')
			tmp_ip = myaddr1[0][4][0]
			#print(myaddr[0][4][0])
			if tmp_ip == ip:
			#if myaddr1[0][4][0] == '127.0.0.1':
				logger.info("域名："+domain+" -> "+ip+" 解析正常")
			else:
				logger.warning("域名解析异常，疑似被劫持，请确认！")
				logger.error("域名："+domain+" -> "+tmp_ip+"，解析异常，请联系管理员核查处理！")
		except ZeroDivisionError:
			logger.exception("域名监测失败！")

if __name__ == "__main__":

	print('''
                                                                                               
 *******    ***   ***   ******               *****   ***                            ***        
 *********  ****  ***  ********             ******** ***                            ***        
 ****  ***  ****  *** ****  ***            ****  *** ***                            ***        
 ****  **** ***** *** ****  ***            ***   *** ***                            ***        
 ****   *** ***** *** ****                 ***   *** ***                            ***        
 ****   *** ***** ***  ****                ***       *********   ******    *******  ***  ****  
 ****   *** *********   *****             ****       ***** ***  ***  ***  **** **** *** ***    
 ****   *** *********     *****           ****       ****  *** ****  **** ***   *** ******     
 ****   *** *** *****       ***           ****   *******   *** **************       *******    
 ****   *** *** ***** ***   ****           ***   *** ***   *** ***       ****       *******    
 ****  **** *** ***** ***   ****           ***   *** ***   *** ****       ***   *** ***  ***   
 **** ****  ***  **** ****  ****           ****  *** ***   ***  ***  **** ***   *** ***  ***   
 ********   ***  ****  ********             *******  ***   ***  ********   *******  ***   ***  
 ******     ***   ***   *****                 ****   ***   ***    *****     *****   ***   **** 

		''')


	#获取监测列表
	domainIP = open_file('domainIP.config')
	t = input("请输入监测频率（秒）：")
	if t.isdigit() and int(t)>0:
		t=int(t)
		logger.add("log/Check_DNS2IP.log",rotation="10 MB")
		logger.info("--- DNS劫持定向监测开始 ---")
		while 1:
			getIP(domainIP)
			time.sleep(t)
	else:
		print("error：请输入大于0的整数！")
		time.sleep(3)
		exit()

