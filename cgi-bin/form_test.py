#!/usr/bin/python3
import sys
import io
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html;charset=UTF-8")
print()
from line_notify_bot import LINENotifyBot
bot = LINENotifyBot(access_token='l0xllBCP6WC4QiI0HThc4zQKZFrDU22bDmiXTO0CVAM')
form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
print("Content-Type: text/html;charset=UTF-8")
print()
print("<html><head></head><body>")
print("<h1>Pythonにform</h1>")
for key in form:
    value = form[key].value
    print("<p> %s: %s </p>" % (key, value))
try:
    name=form["名前"].value
except:
    name=""
try:
    sex=form["性別"].value
except:
    sex=""
try:
    skil=form["スキル"].value
except:
    skil=""
try:
    Business=form["職業"].value
except:
    Business=""
try:
    val=form["問い合わせ"].value
except:
    val=""
try:
    mail=form["メール"].value
except:
    mail=""
try:
    pnum=form["電話"].value
except:
    pnum=""
text="""
お問い合わせ
お名前 %s
性別　 %s
メール %s
電話   %s
業種　 %s
スキル %s
内容
%s
"""
bot.send(message=text % (name,sex,mail,pnum,Business,skil,val))
print("</body></html>")
