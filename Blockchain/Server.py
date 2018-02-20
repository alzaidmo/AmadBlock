# coding=utf-8

import socket
import pickle
import sys

BLU = "\u001b[34;1m"
RST = "\u001b[0m"

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

		print("["+BLU+"Server"+RST+"] Node initialized, listening on port %d" %(self.PortServ))


	def treatReq(self):
		'''Start a service for incoming connections on listenSock'''
		while (True):
			print("["+BLU+"Server"+RST+"] Waiting for incoming connection...\n")
			(SKS, Add) = self.SKL.accept()

			data = bytes.decode(SKS.recv(self.BuffSize))
			typeReq, Req = data.split(' ')[0], data.split(' ')[1] #Splitting request

			if ((Add[0] not in self.Hosts) & (Req != "NEW")):
				print("["+BLU+"Server"+RST+"] Unkown host attempting to connect - Refusing\n")
				SKS.send(b'0')  #Refusing unknown hosts

			else:
				print("["+BLU+"Server"+RST+"] Connection established with %s on port %d" %(Add[0], Add[1]))

				if typeReq == "NODE":
					if Req == "NEW":
						self.addNode(Add)
						SKS.send(b'1') # Confirm successfull treatment of the request					
					elif Req == "CONSENSUS":
						self.consent()
						SKS.send(b'1')
					elif Req == "UPMEM":
						SKS.send(b'1')
						self.updateMem(SKS)
					elif Req == "BLOCKCHAIN":
						self.sendBC(SKS)
					elif Req == "SHUTDOWN":
						self.shutNode(SKS)

				if typeReq == "WEB":
					print("Web Request")
			
			SKS.shutdown(socket.SHUT_RDWR)
			SKS.close()
			print("["+BLU+"Server"+RST+"] Succesfully processed {} request from {}\n".format(Req, Add[0]))



	def addNode(self, Add):
		'''Add an incoming node to the list of trusted hosts'''
		print("["+BLU+"Server"+RST+"] New node reaching out...")
		self.Hosts.add(Add[0])
		print("["+BLU+"Server"+RST+"] Added distant host to known hosts: {}".format(self.Hosts))

	
	def consent(self):
		'''Trigger consesus'''
		print("["+BLU+"Server"+RST+"] Consensus signaled by distant host")
		#self.node.consenter.consent()


	def updateMem(self, SKS):
		'''Update Mempool of current node'''
		print("["+BLU+"Server"+RST+"] New transaction shared by distant host")
		data = SKS.recv(1)
		transaction= b''
		while data:
			transaction += data
			data = SKS.recv(1)

		transaction = pickle.loads(transaction)
		self.node.mempool.add(transaction)
		print("["+BLU+"Server"+RST+"] Updated Mempool: {}".format(self.node.mempool))


	def sendBC(self, SKS):
		'''Send node's BC to distant host'''
		print("["+BLU+"Server"+RST+"] Sending our BC to distant host")
		chain_b = pickle.dumps(self.node.blockchain)
		SKS.send(chain_b)
		print("["+BLU+"Server"+RST+"] BC sent")


	def shutNode(self, SKS):
		'''Shuts the current node'''
		print("["+BLU+"Server"+RST+"] Distant host shutting down node...")
		SKS.send(b'1')
		SKS.shutdown(socket.SHUT_RDWR)
		SKS.close()
		self.SKL.shutdown(socket.SHUT_RDWR)
		self.SKL.close()
		print("["+BLU+"Server"+RST+"] Node shut down\n")
		sys.exit()