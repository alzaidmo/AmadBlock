# coding=utf-8

import socket
import sys

class Server(object):
	"""Server object of a node"""

	def __init__(self, port, node):
		self.node = node
		self.BuffSize = 32
		self.Queue = 3
		self.Hosts = set([])
		self.SKL = 0
		self.IfServ = '0.0.0.0'
		self.PortServ = port


	def startServer(self):
		'''Start a server on Node'''

		'''Init Listening Socket'''
		self.SKL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.SKL.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.SKL.bind((self.IfServ, self.PortServ))
		self.SKL.listen(self.Queue)

		print("[Server] Node initialized, listening on port %d" %(self.PortServ))


	def treatReq(self):
		'''Start a service for incoming connections on listenSock'''
		while (True):
			print("[Server] Waiting for incoming connection...")
			(SKS, Add) = self.SKL.accept()
			
			data = bytes.decode(SKS.recv(self.BuffSize))
			typeReq, Req = data.split(' ')[0], data.split(' ')[1] #Splitting request

			if ((Add[0] not in self.Hosts) & (Req != "NEW")):
				print("[Server] Unkown host attempting to connect - Refusing")
				SKS.send(str.encode("Unknown host, please send NODE NEW request first"))  #Refusing unknown hosts

			else:
				print("[Server] Connection established with %s on port %d" %(Add[0], Add[1]))

				if typeReq == "NODE":
					if Req == "NEW":
						self.addNode(Add)
					elif Req == "CONSENSUS":
						self.consent()
					elif Req == "UPMEM":
						self.updateMem()
					elif Req == "BLOCKCHAIN":
						self.sendBC()
					elif Req == "SHUTDOWN":
						self.shutNode()

				if typeReq == "WEB":
					print("Web Request")
			
			SKS.shutdown(socket.SHUT_RDWR)
			SKS.close()
			print("[Server] Succesfully processed request from %s" %(Add[0]))



	def addNode(self, Add):
		'''Add an incoming node to the list of trusted hosts'''
		print("New node reaching out...")
		self.Hosts.add(Add[0])
		print(self.Hosts)

	
	def consent(self):
		'''Trigger consesus'''
		print("Consensus signaled by distant host")


	def updateMem(self):
		'''Update Mempool of current node'''
		print("New transaction shared by distant host")

	def sendBC(self):
		'''Send node's BC to distant host'''
		print("Sending our BC to distant host")

	def shutNode(self):
		'''Shuts the current node'''
		print("Distant host shutting down node...")
		self.SKL.shutdown(socket.SHUT_RDWR)
		self.SKL.close()
		print("[Server] Node shut down")
		sys.exit()