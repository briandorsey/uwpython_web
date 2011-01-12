
import socket 

#host = 'localhost' 
host = 'block115379-pwc.blueboxgrid.com' 
port = 50000 
size = 1024 
s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port)) 
s.send('Hello, world') 
data = s.recv(size) 
print 'Received:', data
s.close() 

