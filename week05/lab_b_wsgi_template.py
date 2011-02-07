#!/usr/bin/python
import datetime

body = """<html>
<head>
<title>Lab A - CGI experiments</title>
</head>
<body>

The server IP address is %s:%s.<br>
<br>
The server name is %s. (if an IP address, then a DNS problem) <br>
<br>
You are coming from  %s:%s.<br>
<br>
Your hostname is %s.  <br>
<br>
The currenly executing script is %s<br>
<br>
The request arrived at %s<br>


</body>
</html>""" 

def application(environ, start_response):

   response_body = body % (
        environ['SERVER_ADDR'], # server IP
        'bbbb', # server port
        'cccc', # client IP
        'dddd', # client port
        'eeee', # client hostname
        'ffff', # server hostname
        'gggg', # this script name
        'hhhh', # time
        )
   status = '200 OK'

   response_headers = [('Content-Type', 'text/html'),
                       ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]
