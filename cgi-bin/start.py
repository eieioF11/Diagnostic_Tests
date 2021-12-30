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
    <body onLoad=setTimeout(\"location.href=\'../html/index0.html\'\",500)>
        <p>ロード中</p>
        <p>%s</p>
    </body>
</html>
"""
try :
    fpath=os.getcwd()+"\data\ "
    fname=[]
    for f in glob.glob(fpath+'*.csv'):
        fname.append(int(os.path.splitext(os.path.basename(f))[0]))
    #print(fname)
    n=0
    if len(fname):
        n=max(fname)+1
    with open(fpath+str(n)+'.csv', 'w') as f:
        pass
except:
    fpath=__file__.replace('/cgi-bin/start.py', '')+"/data/"
    fname=[]
    for f in glob.glob(fpath+'*.csv'):
        fname.append(int(os.path.splitext(os.path.basename(f))[0]))
    #print(fname)
    n=0
    if len(fname):
        n=max(fname)+1
    #print(html % (fpath,fname))
    with open(fpath+str(n)+'.csv', 'w') as f:
        pass
print(html % (n))