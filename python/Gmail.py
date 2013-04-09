#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2012年9月19日 - 完成模拟点击网页请求ssh账号的功能
# 收取GMAIL指定账户的来自support@alidage.org邮件，分析其中的 SSH账号密码，并给出操作指令

# 已知问题：
# 获取邮件没有匹配账号，密码是guest开始的带有纯数字的字符串，如果阿里大哥改变了这个策略将采集和修改识别方法
# 有时urllib2.openurl请求会包socket 10060错误，具体原因不明
# 增加了paramiko模块实现了远端自动执行指令杀掉已经存在的通道以及重新创建通道

# 从阿里大哥网站请求接受ssh帐号的邮箱和密码
recv_ssh_account_email='test@gmail.com'
recv_ssh_account_email_passwd='test'

# 自动在远端ssh执行创建代理的ssh主机、端口、帐号、密码
ssh_host='www.baidu.com'
ssh_port=22
ssh_account='pi'
ssh_passwd='test'

#################################

import poplib
import email
import string
import base64
import sys,random
import os
import re
import httplib,urllib,urllib2,cookielib
import time
try:
	import win32clipboard as clipboard
	import win32con
	import paramiko
	import Crypto
except ImportError:
	raise


# 处理Referer参考，除第一个页面之外的页面请求时带有上一个页面地址为Referer
# urllib2.BaseHandler不是参数而是class HTTPRefererProcessor继承自urllib2.BaseHandler
class HTTPRefererProcessor(urllib2.BaseHandler):
	def __init__(self):
		self.referer=None

	def http_request(self,request):
		if((self.referer is not None) and not request.has_header("Referer")):
			request.add_unredirected_header("Referer",self.referer)
		return request

	def http_response(self,request,response):
		self.referer=response.geturl()
		return response

	https_request=http_request
	https_response=http_response


def RequestSSH_Mail(email_account):
	try:
		print "模拟浏览器发送账号密码邮件请求...".encode('gb18030')
		user_agent='User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20100101 Firefox/15.0.1'
		cookie=cookielib.CookieJar()
		opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie),HTTPRefererProcessor(),)
		urllib2.install_opener(opener)

		request=urllib2.Request(url='http://alidage.org/')
		request.add_header('User-Agent',user_agent)
		request.add_header('Content-Type','application/x-www-form-urlencoded; charset=UTF-8')
		request.get_method=lambda:'GET'
		urllib2.urlopen(request)

		request=urllib2.Request(url='http://alidage.org/send_trial.php')
		request.add_header('User-Agent',user_agent)
		request.add_header('Referer','http://alidage.org/')
		request.add_header('X-Requested-With','XMLHttpRequest')
		request.add_header('Content-Type','application/x-www-form-urlencoded; charset=UTF-8')
		request.get_method=lambda:'POST'	
		urllib2.urlopen(request,data='email='+urllib.quote(email_account)+'&ajax=true')
		print "获取邮件完成.".encode('gb18030')
		return None
	except urllib2.HTTPError,e:
		print "获取邮件失败,错误码: %d.".encode('gb18030') % e.code
		# raise
		return e.code


def GetSSHPassword(email_account,email_password):
	print "登陆邮箱检查账号密码邮件.".encode('gb18030')
	mailServer=poplib.POP3_SSL('pop.gmail.com')
	mailServer.user(email_account)
	mailServer.pass_(email_password)
	(mailCount,size)=mailServer.stat()
	for i in range(1,mailCount+1):
		(hdr,messages,octet)=mailServer.retr(i)
		body='\n'.encode('utf-8').join(messages)
		mail_from=re.compile(r'(support@alidage.org)')
		mail_match=mail_from.search(body)
		if mail_match and mail_match.group()=='support@alidage.org'.lower() :
			pattern=re.compile(r'(guest[0-9][0-9]*)')	# 获取SSH连接密码
			match=pattern.search(body)
			if match:
				ssh_pwd_alidage=match.group()	# 输出密码
				globals() ["ssh_pwd_alidage"]=ssh_pwd_alidage	# 保存密码到全局变量中
				mailServer.dele(i)	# 获取到密码后，删除邮件
	mailServer.quit()	# 断开服务器连接
	if globals().has_key('ssh_pwd_alidage'):
		# print "ssh_pwd_alidage:%s" % ssh_pwd_alidage
		return ssh_pwd_alidage
	else:
		# print "ssh_pwd_alidage:None."
		return None

def EnvInit():
	reload(sys)
	sys.setdefaultencoding('utf-8')


def OneClickAll():
	global recv_ssh_account_email
	retval=RequestSSH_Mail(recv_ssh_account_email)	# 模拟浏览器点击网页申请密码
	if retval==None:
		print "休眠6秒之后开始获取邮件中的账号和密码".encode('gb18030')
		time.sleep(6)

		max_try=3	# 最多重试三次
		try_timer=0
		while try_timer<max_try:
			global recv_ssh_account_email,recv_ssh_account_email_passwd
			ret=GetSSHPassword(recv_ssh_account_email,recv_ssh_account_email_passwd)
			if ret:
				print "==============================================================="
				print "密码获取成功，请使用如下指令重新创建代理通道".encode('gb18030')
				# 由于需要使用expect登陆ssh，而且ssh本身也需要很长时间才能连接，因此使用了nohup指令，放到后台执行
				cmd=["cd /root/.cronshell/","/bin/kill -9 `/bin/ps aux | /bin/grep s4.alidage.org | /bin/grep -v grep | /bin/awk '{print $2}'`","nohup /root/.cronshell/super_alidage.sh %s &" % ret]
				# 定义需要执行的list
				for index in range(0,len(cmd)):
					print "cmd[%d] %s" % (index,cmd[index])
				print "==============================================================="

				target_cmd="\n".join(cmd)
				SetClipboard(target_cmd)
				print "开始自动远端执行创建指令".encode("gb18030")
				# 获取到密码后自动执行远端指令
				RemoteExec(cmd)
				break
			else:
				# print "==============================================================="
				# print "暂时未获取到密码通知邮件，请稍后再尝试获取邮件通知！".encode('gb18030')
				# print "==============================================================="
				try_timer=try_timer+1
				seconds=random.randint(5,15)
				print "未获取到邮件通知，稍后 %d 秒做第 %d 次尝试.".encode("gb18030") % (seconds,try_timer)
				time.sleep(seconds)
	else:
		print "提交密码请求HTTP发送失败 %s .".encode("gb18030") % requestSSH
				


def OnlyGetMailbySsh():
	global recv_ssh_account_email
	ret=GetSSHPassword(recv_ssh_account_email)
	if ret:
		print "==============================================================="
		print "密码获取成功，请使用如下指令重新创建代理通道".encode('gb18030')
		print "kill -9 `ps aux | grep s4.alidage.org | grep -v grep | awk '{print $2}'`"
		print "./super_alidage.sh %s" % ret
		print "==============================================================="
	else:
		print "==============================================================="
		print "暂时未获取到密码通知邮件，请稍后再尝试获取邮件通知！".encode('gb18030')
		print "如果您尚未请求密码请登录http://alidage.org提交SSH密码请求。".encode('gb18030')
		print "==============================================================="


# 设置剪贴板，需要安装特定扩展才能实现
def SetClipboard(text):
	if sys.platform=="win32":
		clipboard.OpenClipboard()
		clipboard.EmptyClipboard()
		clipboard.SetClipboardData(win32con.CF_TEXT,text)
		clipboard.CloseClipboard()
		print "Unix指令已经复制到剪贴板上".encode('gb18030')


# cmds是所有命令组成的列表(list)，将按照顺序执行
def RemoteExec(cmds):
	print "登陆Linux服务器，重建SSH通道..".encode('gb18030')
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	global ssh_host,ssh_port,ssh_account,ssh_passwd
	ssh.connect(ssh_host,ssh_port,ssh_account,ssh_passwd)
	print "执行如下指令...".encode('gb18030')
	# 由于使用的是另外一个账号登陆的，因此需要切换账号
	stdin,stdout,stderr=ssh.exec_command("/bin/su - root")
	for ci in range(0,len(cmds)):
		print "%s" % cmds[ci]
		stdin,stdout,stderr=ssh.exec_command(cmds[ci])
		# if len(stdout.readlines())!=0:
		# 	print "===========================[EXEC RESULT BEGIN]==========================="
		# 	print "\n".join(stdout.readlines())
		# 	print "============================[EXEC RESULT END]============================"

		# 由于ssh连接需要时间，如果快速断开连接当导致连接创建失败
		# if ci==2:
		# 	print "等待20秒,使代理通道建立".encode("gb18030")
		# 	time.sleep(20)
	# 由于获取的进程号不准确此功能暂时作废
	# stdin,stdout,stderr=ssh.exec_command("/bin/ps aux | /bin/grep s4.alidage.org | /bin/grep -v grep | /bin/awk '{print $2}'")
	# print "新进程号为:%s".encode("gb18030") % stdout.readlines()
	ssh.close()
	print "断开执行指令通道.".encode('gb18030')

def Pause():
	os.system("pause")


def main():
	OneClickAll()

if __name__ == '__main__':
	EnvInit()
	main()
	Pause()
	
