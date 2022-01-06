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
        <meta charset='utf-8'>
        <title>form</title>
		<!--スクリプト読み込み-->
		<link rel="stylesheet" href="../css/style.css" />
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
					src="../image/homeicon.jpeg"
					class="button_home"
					onclick="goClick0()"
					alt="home image"
					width="40"
					height="40"
				/>
				高専生診断テスト
				<img
					src="../image/tool_icon.png"
					class="button_tool"
					onclick="goClick3()"
					alt="tool image"
					width="40"
					height="40"
				/>
			</h1>
		</div>
        <h1>保存されているcsvデータ</h1>
        <p>%s</p>
    </body>
</html>
"""
fpath=__file__.replace('/cgi-bin/show.py', '')+"/data/"
fname=[]
for f in glob.glob(fpath+'*.csv'):
    fname.append(os.path.splitext(os.path.basename(f))[0]+".csv")


print(html % (fname))