#!/usr/bin/env python
import SocketServer
import commands
class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		while True:
			self.data=self.request.recv(1024).strip()
			print "going to run cmd:",self.data
			status,result=commands.getstatusoutput(self.data)
			self.request.sendall(result)
if __name__=="__main__":
	HOST=''
	PORT=9999
	server=SocketServer.TCPServer((HOST,PORT),MyTCPHandler)
	server.serve_forever()
