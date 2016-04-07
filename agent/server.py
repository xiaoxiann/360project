#!/usr/bin/python
import socket
import sys
import argparse
host='localhost'
backlog=5
data_payload=2048
def echo_server(port):
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	server_address=(host,port)	
	sock.bind(server_address)
	sock.listen(backlog)
	while True:
		print "waiting to receive message from client"
		client,address=sock.accept()
		data=client.recv(data_payload)
		if data:
			print "Data:%s"%data
			client.send(data)
			print "send %s bytes back to %s"%(data,address)
		client.close()
if __name__=="__main__":
	parser=argparse.ArgumentParser(description='Socket server Example')
	parser.add_argument('--port',action="store",dest="port",type=int,required=True)
	given_args=parser.parse_args()
	port=given_args.port
	echo_server(port)