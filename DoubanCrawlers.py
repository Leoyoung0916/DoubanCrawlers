#！-*- coding: utf-8 -*-  


#http://pan.baidu.com/share/link?shareid=3283439014&uk=1914119230

import re
import urllib2
import urllib
import string
import os

def getjpgnumrul(url):

	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = {'User-Agent': user_agent}
	req = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(req)
	page = response.read()
	unicodePage = page.decode("utf-8")
	assert page
	ree = r'<a\shref="http://www\.douban\.com/photos/photo/(\d*)/"\sclass=".*?"\stitle=".*?">\n\s*?<img\ssrc=".*?"\s/>'
	pattern = re.compile(ree,re.S)
	jpgnumurl = re.findall(pattern,page)

	return jpgnumurl

def getjpg(url):

	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = {'User-Agent': user_agent}
	req = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(req)
	page = response.read()
	ree = r'<a\sclass="mainphoto"\shref=".*?"\stitle=".*?">\n\s*?<img\ssrc="(.*?)" />'
	pattern = re.compile(ree,re.S)
	jpgrealurl = re.findall(pattern,page)

	return jpgrealurl


print u"""

                            ---豆瓣相册爬虫---

            此爬虫可以爬取制定豆瓣相册中的图片，并保存在制定文件夹中

            作者：杨柳

            版本：1.0

"""

print u"您要爬取哪个豆瓣相册，请输入相册编号"
print u"例如：网址为 http://www.douban.com/photos/album/101360162/的相册，编号为101360162 "

albumurlnum = raw_input()
albumurl = 'http://www.douban.com/photos/album/' + str(albumurlnum) + "/"

stillFolderloop = True

while stillFolderloop:

	print u"您要保存在哪个盘？"
	savedisk = raw_input()
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

y = 0
jpgnumurl=getjpgnumrul(albumurl)
y += 18
if jpgnumurl == []:
	print 'no next page'
x = 1
for i in jpgnumurl:
	s=r'http://www.douban.com/photos/photo/'+ i + r'/'
	jpgurl = getjpg(s)
	print "getting jpg" + str(x)
	urllib.urlretrieve(jpgurl[0], savedisk.capitalize() + r':\\' + savefolder + r'\\%s.jpg' %x)
	x+=1

while True:
	try:
		print ""
		print "getting page" + str(y/18 + 1)
		jpgnumurl=getjpgnumrul(albumurl+"?start=" + str(y))
		y += 18
		if jpgnumurl == []:
			print 'no next page'
			print "end"
			break
		for i in jpgnumurl:
			s=r'http://www.douban.com/photos/photo/'+ i + r'/'
			jpgurl = getjpg(s)
			print "getting jpg" + str(x)
			urllib.urlretrieve(jpgurl[0], savedisk.capitalize() + r':\\' + savefolder + r'\\%s.jpg' %x)
			x+=1
	except:
		print "problem!"
		break



