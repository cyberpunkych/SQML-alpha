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

Firstly you need to initialize the html_parser module:<br>
<code>\>\>\>import html_parser<br>
\>\>\>A = html_parser.Parser()<br>
\>\>\>
</code>

Next, you should load your webpage or html file:<br>
<code>\>\>\>page = urllib.urlopen('http://habrahabr.ru/').read()<br>
\>\>\>
</code>

And then, load it in the module:<br>
<code>\>\>\>A.load(page)<br>
\>\>\>
</code>

Ok! And now you can make SQL-like requests to this source, and parse it:<br>
<code>\>\>\>A.query("SELECT @class FROM a WHERE @class=='hub '")
\>\>\>A.value<br>
{'class': ['hub ']}<br>
\>\>\>A.value['class']<br>
['hub ']<br>
\>\>\>A.result<br>
[['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '],
 ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub ']]<br>
\>\>\>
</code>