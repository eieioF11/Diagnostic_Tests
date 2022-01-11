#!/usr/bin/python3
import sys
import io
import csv
import os
import glob
import cgi
import cgitb
import pandas as pd
cgitb.enable()
import matplotlib.pyplot as plt

print("Content-Type: text/html;charset=UTF-8")
print()

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
		<h1>統計</h1>
		<p>アクセス数</p>
        <p> %s </p>
        <p>ヒストグラム</p>
        <img src='../data/Statistics/hist.png' style="display: block; margin: auto;">
        <p>平均高専生度</p>
        <p> %s </p>
        <p> 最大 %s 最小 %s</p>
        <p>男女比</p>
        <p> 男性 %s人 女性%s人</p>
    </body>
</html>
"""
try :
    fpath=os.getcwd()+"\\data\\Statistics\\"
    df = pd.read_csv(fpath+'data.csv',names=['sex', 'score'])
except:
    fpath=__file__.replace('/cgi-bin/Statistics.py', '')+"/data/Statistics/"
    df = pd.read_csv(fpath+'data.csv',names=['sex', 'score'])

#df.hist()
plt.hist(df['score'].tolist(), bins=16)
plt.savefig(fpath+'hist.png')
mean=float(df.mean())
max=float(df['score'].max())
min=float(df['score'].min())
df_m = (df["sex"] == 'm')
df_f = (df["sex"] == 'f')
m=df_m.sum()
f=df_f.sum()

print(html % (len(df),mean,max,min,m,f))