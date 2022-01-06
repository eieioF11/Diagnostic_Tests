#!/usr/bin/python3
import sys
import io
import csv
import os
import glob
import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html;charset=UTF-8")
print()

form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
print("Content-Type: text/html;charset=UTF-8")
html="""
<html>
    <head>
        <title>処理</title>
    </head>
    <body onLoad=setTimeout(\"location.href=\'../html/index_tool.html\'\",500)>
        <p>削除中</p>
        <p>%s delete</p>
    </body>
</html>
"""
fpath=__file__.replace('/cgi-bin/delete.py', '')+"/data/"
fname=[]
for f in glob.glob(fpath+'*.csv'):
    fname.append(os.path.splitext(os.path.basename(f))[0]+".csv")
for f in fname:
    os.remove(fpath+f)

print(html%(fname))