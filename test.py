#!/usr/bin/env python
import urllib
import html_parser
page = urllib.urlopen('http://m.habrahabr.ru/post/147682/').read()
A = html_parser.Parser()
A.load(page)
A.query('SELECT WORD @@content, WORD name FROM a')
print A.value['@@content']
print A.value['name']