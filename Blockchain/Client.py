# coding=utf-8

import socket
import pickle
import sys

MAG = "\u001b[35;1m"
RST = "\u001b[0m"

class Client(object):
	"""Client part of the node responsible for sending inter-node requests"""
	def __init__(self, name):
		self.SK = 0  #Inter-node communication socket
		self.name = name
		

	def conToNode(self, nodeIP, nodePort):
		'''Connects to Node at nodeIP on port nodePort'''
		self.SK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.SK.connect((nodeIP, nodePort))
		print("["+MAG+self.name+" Client"+RST+"] Connection successfully established with %s" %(nodeIP))

	def newReq(self):
		'''Declares self as a new node entering the network'''
		print("["+MAG+self.name+" Client"+RST+"] Making 1st contact")
		self.SK.send(str.encode("NEW")) #New node declaration
		response = self.SK.recv(1)
		if response == b'1':
			print("["+MAG+self.name+" Client"+RST+"] Server treated request successfully ({})".format(response.decode("utf-8")))
		else:
			print("["+MAG+self.name+" Client"+RST+"] Server signaled a problem ({})".format(response.decode("utf-8")))
		self.SK.shutdown(socket.SHUT_WR)
		#self.SK.close()
		print("["+MAG+self.name+" Client"+RST+"] Ended communication client side\n")

	def consReq(self):
		'''Signals an onging consensus to other nodes'''
		print("["+MAG+self.name+" Client"+RST+"] Asking for consensus")	
		self.SK.send(str.encode("CONSENSUS")) #Consensus request
		response = self.SK.recv(1)
		if response == b'1':
			print("["+MAG+self.name+" Client"+RST+"] Server treated request successfully ({})".format(response.decode("utf-8")))
		else:
			print("["+MAG+self.name+" Client"+RST+"] Server signaled a problem ({})".format(response.decode("utf-8")))
		self.SK.shutdown(socket.SHUT_WR)
		#self.SK.close()
		print("["+MAG+self.name+" Client"+RST+"] Ended communication client side\n")


	def getBC(self):
		'''Gets Blockchain from distant host'''
		self.SK.send(str.encode("BLOCKCHAIN"))
		print("["+MAG+self.name+" Client"+RST+"] Asking for Blockchain")
		
		response = self.SK.recv(1)
		data = b''
		while response :
			data += response
			response = self.SK.recv(1)
	
		print("{DATA client} - " + str(data [:10]) + "..." + str(data [-10:]))
		chain = pickle.loads(data)
		for block in chain:
			print("["+MAG+self.name+" Client"+RST+"] Received {}".format(block))
		self.SK.shutdown(socket.SHUT_WR)
		#self.SK.close()
		print("["+MAG+self.name+" Client"+RST+"] Ended communication client side\n")
		
		return chain


	def webTrans(self, transaction):
		'''Shares a transaction to other nodes'''
		print("["+MAG+self.name+" Client"+RST+"] Sending new transaction")
		transaction_b = pickle.dumps(transaction)
		self.SK.send(transaction_b)

		print("["+MAG+self.name+" Client"+RST+"] Sent new transaction {}".format(transaction))
		
		self.SK.shutdown(socket.SHUT_WR)
		#self.SK.close()
		print("["+MAG+self.name+" Client"+RST+"] Ended communication client side\n")



	#def memReq(self, transaction):
	#	'''Shares a .er nodes'''
	#	print("["+MAG+self.name+" Client"+RST+"] Offering mempool update")
	#	self.SK.send(str.encode("UPMEM")) #Mempool update request
	#	response = self.SK.recv(1)
	#	if response == b'1':
	#		print("["+MAG+self.name+" Client"+RST+"] Server interpreted request successfully ({})".format(response.decode("utf-8")))
	#		transaction_b = pickle.dumps(transaction)
	#		self.SK.send(transaction_b)
	#		print("["+MAG+self.name+" Client"+RST+"] Shared new transaction {}".format(transaction))
	#	else:
	#		print("["+MAG+self.name+" Client"+RST+"] Server signaled a problem ({})".format(response.decode("utf-8")))		
	#	self.SK.shutdown(socket.SHUT_WR)
	#	#self.SK.close()
	#	print("["+MAG+self.name+" Client"+RST+"] Ended communication client side\n")


#	def shutNode(self):
#		'''[DEBUG ONLY] Shuts distant host server down'''
#		print("["+MAG+self.name+" Client"+RST+"] Shutting down distant host")
#		self.SK.send(str.encode("SHUTDOWN"))
#		response = self.SK.recv(1)
#		if response == b'1':
#			print("["+MAG+self.name+" Client"+RST+"] Server treated request successfully ({})".format(response.decode("utf-8")))
#		else:
#			print("["+MAG+self.name+"Client"+RST+"] Server signaled a problem ({})".format(response.decode("utf-8")))
#		print("["+MAG+self.name+"Client"+RST+"] Distant node shut down\n")


