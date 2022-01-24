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
		<link rel="stylesheet" href="../css/style_e.css" />
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
        <p>
            %s
            <img src='../image/%s.png' style="display: block; margin: auto;">
            %s
        </p>
        <h2>
            参考
            <img src='../image/診断結果.png' style="display: block; margin: auto;">
        </h2>
    </body>
</html>

"""
ip=0
iptext=""
if "REMOTE_ADDR" in os.environ:
    iptext=os.environ["REMOTE_ADDR"]
    iptext=iptext.split('.')
    ip=int(iptext[3])

for key in form:
    value = form[key].value

sex="m"

try :
    fpath=os.getcwd()+"\data\ "
    #fname=[]
    #for f in glob.glob(fpath+'*.csv'):
    #    fname.append(int(os.path.splitext(os.path.basename(f))[0]))
    ##print(fname)
    #n=0
    #if len(fname):
    #    n=max(fname)

    with open(fpath+str(ip)+'.csv','r') as f:
        reader = csv.reader(f)
        crow=[row for row in reader]
        tr=[]
        for vector in crow:
            try:
                v=int(vector[0])
            except:
                sex=str(vector[0])
                v=None
            if v!=None:
                tr.append (vector[0])
        data = list(map(int,tr))
except:
    fpath=__file__.replace('/cgi-bin/end.py', '')+"/data/"
    #fname=[]
    #for f in glob.glob(fpath+'*.csv'):
    #    fname.append(int(os.path.splitext(os.path.basename(f))[0]))
    ##print(fname)
    #n=0
    #if len(fname):
    #    n=max(fname)

    with open(fpath+str(ip)+'.csv', 'r') as f:
        reader = csv.reader(f)
        crow=[row for row in reader]
        tr=[]
        for vector in crow:
            try:
                v=int(vector[0])
            except:
                sex=str(vector[0])
                v=None
            if v!=None:
                tr.append (vector[0])
        data = list(map(int,tr))

data.append(int(value))
Score=sum(data)
try:
    with open(fpath+"Statistics/data.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow([sex,Score])
except:
    pass

im=1
text="あなたは"
if Score >= 81:
    text+="プロ高専生です"
    im=5
elif Score >= 61:
    text+="アマチュア高専生です"
    im=4
elif Score >= 41:
    text+="高専入学一ヶ月の人です"
    im=3
elif Score >= 21:
    text+="高専生向き一般人です"
    im=2
else:
    text+="健全な一般人です"
    im=1

print(html % (Score,im,text))
