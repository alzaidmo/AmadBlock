# coding=utf-8

import socket
import sys

BuffSize = 32
QueuedCo = 3
Nodes = set([]) #set instead of list to avoid duplicates

def startNode():
	'''Start a server on Node'''
	IPServ = '0.0.0.0'
	PortServ = 4242

	'''Init Listening Socket'''
	SKL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	SKL.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	SKL.bind((IPServ, PortServ))
	SKL.listen(QueuedCo)

	print("[OK] Node initialized")

	return SKL

def serveNode(listenSock):
	'''Start a service for incoming connections on listenSock'''
	while (True):
		print("Waiting for incoming connection...")
		(SKS, Add) = listenSock.accept()
		
		data = bytes.decode(SKS.recv(BuffSize))
		ReqType, Req = data.split(' ')[0], data.split(' ')[1] #Splitting request

		if ((Add[0] not in Nodes) & (Req != "NEW")):
			print("Unkown node attempting to connect - Refusing")
			SKS.send(str.encode("Unknown Node, please send NODE NEW request first"))  #Refusing unknown nodes

		else:
			print("Connection established with %s on port %d" %(Add[0], Add[1]))
			
			if ReqType == "NODE":
				print("Node request")
				if Req == "SHUTDOWN":
					SKS.shutdown(socket.SHUT_RDWR)
					SKS.close()
					shutNode(listenSock)
				if Req == "NEW":
					print("New node reaching out...")
					Nodes.add(Add[0])
					print(Nodes)

			while (data):
				print("Client >>>", data)
				SKS.send(str.encode(data)) #Echo to client
				data = SKS.recv(BuffSize)
		
		SKS.shutdown(socket.SHUT_RDWR)
		SKS.close()
		print("Ended connection with %s" %(Add[0]))


def shutNode(listenSock):
	'''Shutdown & Close all sockets, close node'''
	print("Shutting down node...")
	listenSock.shutdown(socket.SHUT_RDWR)
	listenSock.close()
	print("[OK] Node shut down")
	sys.exit()


if __name__ == "__main__":
	SKL = startNode()
	serveNode(SKL)

