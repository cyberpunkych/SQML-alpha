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
<code><br>\>\>\>import html_parser<br>
\>\>\>A = html_parser.Parser()<br>
\>\>\>
</code>

Next, you should load your webpage or html file:<br>
<code><br>\>\>\>page = urllib.urlopen('http://habrahabr.ru/').read()<br>
\>\>\>
</code>

And then, load it in the module:<br>
<code><br>\>\>\>A.load(page)<br>
\>\>\>
</code>

Ok! And now you can make SQL-like requests to this source, and parse it:<br>
<code><br>\>\>\>A.query("SELECT @class FROM a WHERE @class=='hub '")<br>
\>\>\>A.value<br>
{'class': ['hub ']}<br>
\>\>\>A.value['class']<br>
['hub ']<br>
\>\>\>A.result<br>
[['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '],
 ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub '], ['hub ']]<br>
\>\>\>
</code>


More SQL-like examples:
=======================

<code><br>
SELECT @@content FROM title // Get the text from "title" tag<br>
SELECT @href FROM a // Get the "href" value from "a" tag<br>
SELECT @@content, @href FROM a WHERE @class=='test-class' // Get text and "href" value from tag a, where class value is "test-class"<br>
SELECT @id FROM input WHERE @maxlength>5 // Get "id" value from "input" tag, where "maxlength" value more than 5<br>
SELECT @class FROM div WHERE len(@id)!=0 // Yes, you can use python functions for string in conditionals<br>
</code>

Questions?
==========

You can ask me, or cyberguru007 anything about this project!