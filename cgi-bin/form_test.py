#!/usr/bin/python3
import sys
import io
import cgi
form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
print("Content-Type: text/html;charset=UTF-8")
print()
print("<html><head></head><body>")
print("<h1>Pythonにform</h1>")
for key in form:
    value = form[key].value
    print("<p> %s: %s </p>" % (key, value))
print("</body></html>")