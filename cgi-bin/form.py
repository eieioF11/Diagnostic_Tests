#!/usr/bin/python3
import sys
import io
import csv
import os
import glob
import cgi
form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
print("Content-Type: text/html;charset=UTF-8")
html="""
<html>
    <head>
        <title>処理</title>
    </head>
    <body onLoad=setTimeout(\"location.href=\'../html/index%s.html\'\",500)>
        <p>ロード中</p>
        <p> %s </p>
    </body>
</html>
"""
for key in form:
    value = form[key].value

try :
    fpath=os.getcwd()+"\data\ "
    fname=[]
    for f in glob.glob(fpath+'*.csv'):
        fname.append(int(os.path.splitext(os.path.basename(f))[0]))
    #print(fname)
    n=0
    if len(fname):
        n=max(fname)

    with open(fpath+str(n)+'.csv','r') as f:
        reader = csv.reader(f)
        crow=[row for row in reader]
        tr=[]
        for vector in crow:
            tr.append (vector[0])
        data = list(map(int,tr))

    with open(fpath+str(n)+'.csv', 'a' ,newline='') as f:
        writer = csv.writer(f)
        writer.writerow(value)

except:
    fpath="../data/"
    fname=[]
    for f in glob.glob(fpath+'*.csv'):
        fname.append(int(os.path.splitext(os.path.basename(f))[0]))
    #print(fname)
    n=0
    if len(fname):
        n=max(fname)

    with open(fpath+str(n)+'.csv', 'r') as f:
        reader = csv.reader(f)
        crow=[row for row in reader]
        tr=[]
        for vector in crow:
            tr.append (vector[0])
        data = list(map(int,tr))

    with open(fpath+str(n)+'.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(form)

dlen=len(data)+1

print(html % (dlen,value))
