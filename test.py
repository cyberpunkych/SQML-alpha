#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import html_parser
page = urllib.urlopen('http://habrahabr.ru/').read()
A = html_parser.Parser()
A.load(page)
A.query("SELECT @title, @@content FROM a WHERE @class=='hub '")
print A.result
