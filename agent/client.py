
#!/usr/bin/env python
import socket
HOST='localhost'
PORT=9999
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
	user_input=raw_input('your message').strip()
	if len(user_input)==0:
		continue
	s.sendall(user_input)
	print 'sending ....'
	data=s.recv(1024)
	print 'recevied',data
s.close()
