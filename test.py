<<<<<<< HEAD
#!/usr/bin/env python
import urllib
import html_parser
page = urllib.urlopen('http://m.habrahabr.ru/post/147682/').read()
A = html_parser.Parser()
A.load(page)
A.query('SELECT WORD @@content, WORD name FROM a')
print A.value['name']
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import html_parser
page = urllib.urlopen('http://habrahabr.ru/').read()
A = html_parser.Parser()
A.load(page)
A.query("SELECT @title, @@content FROM a WHERE @class=='hub '")
print A.result

>>>>>>> e80a5218d724dc95c5a445f80b52f0bb1960461c
