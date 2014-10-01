#！-*- coding: utf-8 -*-  


#http://pan.baidu.com/share/link?shareid=3283439014&uk=1914119230

import re
import urllib2
import urllib
import string
import os
import sys
import requests
import cookielib

## 这段代码是用于解决中文报错的问题  
reload(sys)
sys.setdefaultencoding("utf-8")  
#####################################################
#登录人人
loginurl = 'http://www.renren.com/PLogin.do'
logindomain = 'renren.com'

class Login(object):
    
    def __init__(self):
        self.name = ''
        self.passwprd = ''
        self.domain = ''

        self.cj = cookielib.LWPCookieJar()            
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj)) 
        urllib2.install_opener(self.opener)
    
    def setLoginInfo(self,username,password,domain):
        '''设置用户登录信息'''
        self.name = username
        self.pwd = password
        # self.domain = domain

    def login(self):
        '''登录网站 'domain':self.domain,'''
        loginparams = {'email':self.name, 'password':self.pwd}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'}
        req = urllib2.Request(loginurl, urllib.urlencode(loginparams),headers=headers)   #loginurl = 'http://www.renren.com/PLogin.do'
        # urllib2.Request(url[, data][, headers][, origin_req_host][, unverifiable])
        response = urllib2.urlopen(req)
        # self.operate = self.opener.open(req)
        thePage = response.read()

        # print thePage
        



def getjpgnumrul(url):
	# print url
	user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'
	headers = {'User-Agent': user_agent}
	req = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(req)
	page = response.read()

	assert page

	# <a href="http://photo.renren.com/photo/397859534/photo-7663358623" class="picture">

	ree = r'<a\s\shref="(http://photo\.renren\.com/photo/\d*?/photo-[^"]*?)"\sclass="picture">'
	pattern = re.compile(ree,re.S)
	jpgnumurl = re.findall(pattern,page)
	# print jpgnumurl
	return jpgnumurl

def getjpg(url):

	user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'
	headers = {'User-Agent': user_agent}
	req = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(req)
	page = response.read()



	ree = r'<img\sid="photo"\ssrc="(.*?\.jpg)"\stitle=""\s/>'
	pattern = re.compile(ree,re.S)
	jpgrealurl = re.findall(pattern,page)

	return jpgrealurl




if __name__ == '__main__': 	 
	userlogin = Login()
	username = 'leoyoung0916@gmail.com'
	password = 'qlzx6cg8'
	domain = logindomain  #logindomain = 'renren.com'
	userlogin.setLoginInfo(username,password,domain)
	userlogin.login()

	print u"""

	                            ---人人相册爬虫---

	            此爬虫可以爬取制定人人相册中的图片，并保存在制定文件夹中

	            作者：杨柳

	            版本：1.0

	"""

	print u"您要爬取哪个人人相册，请输入相册网址"
	print u"例如：http://photo.renren.com/photo/474268198/album-1064581091"

	albumurl1 =raw_input()
	albumurl = albumurl1 + "?noPager=1"
	stillFolderloop = True


	print u"您要保存在哪个盘？"
	savedisk = raw_input()

	while stillFolderloop:
		print u"您要保存在" + savedisk.capitalize() + u"盘的哪个文件夹下"
		savefolder = raw_input()
		ifexist = os.path.exists(savedisk.capitalize() + r':\\' + savefolder)
		if ifexist:
			print u"您指定的目录已经存在了，爬取文件可能会覆盖同名文件，确认此文件夹吗？"
			while True:
				s = raw_input("y/n  ")
				if s == 'y':
					stillFolderloop = False
					break
				elif s == 'n':
					stillFolderloop = True
					break
				else:
					pass
		else:
			stillFolderloop = False
			os.makedirs(savedisk.capitalize() + r':\\' + savefolder)

	print u"文件将保存在" + savedisk.capitalize() + u"盘的" + savefolder + u"文件夹下"




	jpgnumurl=getjpgnumrul(albumurl)
	print jpgnumurl
	# f = open('page.txt')
	# try:
	# 	f.write(jpgnumurl)
	# finally:
	# 	f.close()

	globaljpgnumurl = jpgnumurl
	if jpgnumurl == []:
		print 'no next page'
	print "getting page1"
	x = 1
	for i in jpgnumurl:
		jpgurl = getjpg(i)
		print "getting jpg" + str(x)
		# print jpgurl
		urllib.urlretrieve(jpgurl[0], savedisk.capitalize() + r':\\' + savefolder + r'\\%s.jpg' %x)
		x+=1

	# page = 2
	# while True:
	# 	try:
	# 		print ""
	# 		print "getting page" + str(page)
	# 		jpgnumurl=getjpgnumrul(albumurl+"#page"+str(page))
	# 		if jpgnumurl == globaljpgnumurl:
	# 			print jpgnumurl
	# 			# f = open('page2.txt')
	# 			# try:
	# 			# 	f.write(jpgnumurl)
	# 			# finally:
	# 			# 	f.close()
	# 			print "no next pages"
	# 			break
	# 		globaljpgnumurl = jpgnumurl
	# 		page += 1
	# 		if jpgnumurl == []:
	# 			print 'no next page'
	# 			print "end"
	# 			break
	# 		for i in jpgnumurl:
	# 			jpgurl = getjpg(i)
	# 			print "getting jpg" + str(x)
	# 			urllib.urlretrieve(jpgurl[0], savedisk.capitalize() + r':\\' + savefolder + r'\\%s.jpg' %x)
	# 			x+=1
	# 	except:
	# 		print "problem!"
	# 		break



