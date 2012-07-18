SQML-alpha
==========

SQML-alpha repository


It will be the small module for python, which can help you to parse html data.<br>
You can do than without regexp and other brainfucking things. <br>
Only SQL-like syntax. Nothing more ;)<br>

How i can use it?
=================

It is very simple! Just look in <b>test.py</b> file ;)


No! I need more instructions!
=============================

Okay, let's start.

Firstly you need to initialize the html_parser module:

<code>
>>>import html_parser
>>>A = html_parser.Parser()
>>>
</code>

Next, you should load your webpage or html file:
<code>
>>>page = urllib.urlopen('http://habrahabr.ru/').read()
>>>
</code>

And then, load it in the module:
<code>
>>>A.load(page)
</code>

Ok! And now you can make SQL-like requests to this source, and parse it:
<code>
>>>A.query("SELECT @class FROM a WHERE @class=='hub '")
>>>A.value
{'class': ['hub ']}
>>>A.value['class']
['hub ']
>>>A.result
[['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '],
 ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub ']]
>>>
</code>