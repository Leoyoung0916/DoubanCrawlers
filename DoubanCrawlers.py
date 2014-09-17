# -*- coding: utf-8 -*-  

import re
import urllib2
import urllib
import string


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

	
jpgnumurl=getjpgnumrul('http://www.douban.com/photos/album/128056017/')
x = 0
for i in jpgnumurl:
	s=r'http://www.douban.com/photos/photo/'+ i + r'/'
	jpgurl = getjpg(s)
	urllib.urlretrieve(jpgurl[0], r'F:\DoubanPhotos\%s.jpg' %x)
	x+=1

y = 18
while True:
	try:
		jpgnumurl=getjpgnumrul('http://www.douban.com/photos/album/128056017/'+"?start=" + str(y))
		y += 18
		print jpgnumurl
		if jpgnumurl == []:
			print 'no next page'
			break
		x = 0
		for i in jpgnumurl:
			s=r'http://www.douban.com/photos/photo/'+ i + r'/'
			print s
			jpgurl = getjpg(s)
			print jpgurl
			urllib.urlretrieve(jpgurl[0], r'F:\DoubanPhotos\%s.jpg' %x)
			x+=1
	except:
		print 'no next page'
		break



