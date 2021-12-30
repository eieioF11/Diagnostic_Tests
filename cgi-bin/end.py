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
        <meta charset='utf-8'>
        <title>form</title>
		<!--スクリプト読み込み-->
		<link rel="stylesheet" href="../css/style2.css" />
        <script src="../js/button.js"></script>
		<!--Icon-->
		<link
			rel="shortcut icon"
			href="../image/F11icon32x32.ico"
			type="image/vnd.microsoft.icon"
		/>
    </head>
    <body>
		<!--タイトル-->
		<div class="TITLE">
			<h1>
				<img
					src="../image/sangirogo.png"
					class="button_school"
					onclick="goClick1()"
					alt="School image"
					width="40"
					height="40"
				/>
				高専生診断テスト
				<img
					src="../image/homeicon.jpeg"
					class="button_home"
					onclick="goClick0()"
					alt="home image"
					width="40"
					height="40"
				/>
			</h1>
		</div>
		<h1>結果</h1>
		<p>あなたの高専生度は</p>
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
except:
    fpath=__file__.replace('/cgi-bin/end.py', '')+"/data/"
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

data.append(int(value))
Score=sum(data)

print(html % (Score))
