#!/usr/bin/python
import time
import datetime


html = """<html>
<head></head>
    <body>
        <p>Here is the time: %s</p>
        <p>and again: %s</p>
    </body>
</html>
""" % (time.time(), datetime.datetime.now())

print "Content-Type: text/html"
print
print html
