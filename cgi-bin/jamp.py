#!/usr/bin/python3
import sys
import io
import cgi
form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
print("Content-Type: text/html;charset=UTF-8")
html="""
<html>
    <head>
        <title>処理</title>
    </head>
    <body onLoad=setTimeout(\"location.href=\'../html/index_sex.html\'\",10)>
        <p>ロード中</p>
    </body>
</html>
"""
print(html)