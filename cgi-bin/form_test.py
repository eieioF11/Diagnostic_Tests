#!/usr/bin/python3
import sys
import io
import cgi
from line_notify_bot import LINENotifyBot
bot = LINENotifyBot(access_token='l0xllBCP6WC4QiI0HThc4zQKZFrDU22bDmiXTO0CVAM')
form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
print("Content-Type: text/html;charset=UTF-8")
print()
print("<html><head></head><body>")
print("<h1>Pythonにform</h1>")
text=""
for key in form:
    value = form[key].value
    print("<p> %s: %s </p>" % (key, value))
    text=str(key)+":"+str(value)
bot.send(message=text)
print("</body></html>")
