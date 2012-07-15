#!/usr/bin/python
#coding: utf8
__author__ = "cyber-punk"

import urllib
import re




url = "http://m.habrahabr.ru/"
answ = urllib.urlopen(url)
answ = answ.read()
regexp = re.findall('class="t">(.*)</a>', answ)
regexp2 = re.findall('<a href="(.*)" class="t"', answ)


for i in xrange(len(regexp2)):
	url = regexp2[i]
	print url
	answ = urllib.urlopen(url)
	answ = answ.read()
	regexp3 = re.findall('<div class="txt">(.*)</div>', answ)
	print regexp3