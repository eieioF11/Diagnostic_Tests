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

name=form["名前"].value
sex=form["性別"].value
skil=form["スキル"].value
Business=form["職業"].value
val=form["問い合わせ"].value
mail=form["メール"].value
pnum=form["電話"].value
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
