# coding=utf-8

import socket
import sys

class Server(object):
	"""Server object of a node"""

	def __init__(self, port = 4242):
		self.BuffSize = 32
		self.Queue = 3
		self.Nodes = set([])
		self.SKL = 0
		self.IPServ = '0.0.0.0'
		self.PortServ = port


	def startNode(self):
		'''Start a server on Node'''

		'''Init Listening Socket'''
		self.SKL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.SKL.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.SKL.bind((self.IPServ, self.PortServ))
		self.SKL.listen(self.Queue)

		print("[OK] Node initialized, listening on port %d" %(self.PortServ))


	def acceptReq(self):
		'''Start a service for incoming connections on listenSock'''
		while (True):
			print("[OK] Waiting for incoming connection...")
			(SKS, Add) = self.SKL.accept()
			
			data = bytes.decode(SKS.recv(self.BuffSize))
			typeReq, Req = data.split(' ')[0], data.split(' ')[1] #Splitting request

			if ((Add[0] not in self.Nodes) & (Req != "NEW")):
				print("[WARNING] Unkown host attempting to connect - Refusing")
				SKS.send(str.encode("Unknown host, please send NODE NEW request first"))  #Refusing unknown nodes

			else:
				print("[OK] Connection established with %s on port %d" %(Add[0], Add[1]))

				if typeReq == "NODE":
					if Req == "NEW":
						self.addNode(Add)
					if Req == "CONSENSUS":
						self.consent()
					if Req == "UPMEM":
						self.updateMem()
					if Req == "SHUTDOWN":
						self.shutNode()

				if typeReq == "WEB":
					print("Web Request")
			
			SKS.shutdown(socket.SHUT_RDWR)
			SKS.close()
			print("[OK] Succesfully processed request from %s" %(Add[0]))



	def addNode(self, Add):
		'''Add an incoming node to the list of trusted hosts'''
		print("New node reaching out...")
		self.Nodes.add(Add[0])
		print(self.Nodes)

	
	def consent(self):
		'''Trigger consesus'''
		print("Consensus request")


	def updateMem(self):
		'''Update Mempool of current node'''
		print("Mempool update request")


	def shutNode(self):
		'''Shuts the current node'''
		print("Shutting down node...")
		self.SKL.shutdown(socket.SHUT_RDWR)
		self.SKL.close()
		print("[OK] Node shut down")
		sys.exit()