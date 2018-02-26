# coding=utf-8

import socket
import pickle
import sys

MAG = "\u001b[35;1m"
RST = "\u001b[0m"

class Client(object):
	"""Client part of the node responsible for sending inter-node requests"""
	def __init__(self):
		self.SK = 0  #Inter-node communication socket
		

	def conToNode(self, nodeIP, nodePort):
		'''Connects to Node at nodeIP on port nodePort'''
		self.SK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.SK.connect((nodeIP, nodePort))
		print("["+MAG+"Client"+RST+"] Connection successfully established with %s" %(nodeIP))

	def newReq(self):
		'''Declares self as a new node entering the network'''
		print("["+MAG+"Client"+RST+"] Making 1st contact")
		self.SK.send(str.encode("NODE NEW")) #New node declaration
		response = self.SK.recv(1)
		if response == b'1':
			print("["+MAG+"Client"+RST+"] Server treated request successfully ({})\n".format(response.decode("utf-8")))
		else:
			print("["+MAG+"Client"+RST+"] Server signaled a problem ({})\n".format(response.decode("utf-8")))
		self.SK.shutdown(socket.SHUT_RDWR)
		self.SK.close()
		print("["+MAG+"Client"+RST+"] Ended communication client side\n")

	def consReq(self):
		'''Signals an onging consensus to other nodes'''
		print("["+MAG+"Client"+RST+"] Asking for consensus")	
		self.SK.send(str.encode("NODE CONSENSUS")) #Consensus request
		response = self.SK.recv(1)
		if response == b'1':
			print("["+MAG+"Client"+RST+"] Server treated request successfully ({})\n".format(response.decode("utf-8")))
		else:
			print("["+MAG+"Client"+RST+"] Server signaled a problem ({})\n".format(response.decode("utf-8")))
		self.SK.shutdown(socket.SHUT_RDWR)
		self.SK.close()
		print("["+MAG+"Client"+RST+"] Ended communication client side\n")

	def memReq(self, transaction):
		'''Shares a new transaction with the other nodes'''
		print("["+MAG+"Client"+RST+"] Offering mempool update")
		self.SK.send(str.encode("NODE UPMEM")) #Mempool update request
		response = self.SK.recv(1)
		if response == b'1':
			print("["+MAG+"Client"+RST+"] Server interpreted request successfully ({})".format(response.decode("utf-8")))
			transaction_b = pickle.dumps(transaction)
			self.SK.send(transaction_b)
			print("["+MAG+"Client"+RST+"] Shared new transaction {}\n".format(transaction))
		else:
			print("["+MAG+"Client"+RST+"] Server signaled a problem ({})\n".format(response.decode("utf-8")))		
		self.SK.shutdown(socket.SHUT_RDWR)
		self.SK.close()
		print("["+MAG+"Client"+RST+"] Ended communication client side\n")		

	def getBC(self):
		'''Gets Blockchain from distant host'''
		self.SK.send(str.encode("NODE BLOCKCHAIN"))
		print("["+MAG+"Client"+RST+"] Asking for Blockchain")
		
		response = self.SK.recv(1)
		data = b''
		while response :
			data += response
			response = self.SK.recv(1)
	
		chain = pickle.loads(data)
		print("["+MAG+"Client"+RST+"] End of stream, received {}\n".format(chain))
		self.SK.shutdown(socket.SHUT_RDWR)
		self.SK.close()
		print("["+MAG+"Client"+RST+"] Ended communication client side\n")


#	def shutNode(self):
#		'''[DEBUG ONLY] Shuts distant host server down'''
#		print("["+MAG+"Client"+RST+"] Shutting down distant host")
#		self.SK.send(str.encode("NODE SHUTDOWN"))
#		response = self.SK.recv(1)
#		if response == b'1':
#			print("["+MAG+"Client"+RST+"] Server treated request successfully ({})".format(response.decode("utf-8")))
#		else:
#			print("["+MAG+"Client"+RST+"] Server signaled a problem ({})".format(response.decode("utf-8")))
#		print("["+MAG+"Client"+RST+"] Distant node shut down\n")