# coding=utf-8

import socket
import sys

class Client(object):
	"""Client part of the node responsible for sending inter-node requests"""
	def __init__(self):
		self.SK = 0  #Inter-node communication socket
		

	def conToNode(self, nodeIP, nodePort):
		'''Connects to Node at nodeIP on port nodePort'''
		self.SK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.SK.connect((nodeIP, nodePort))
		print("[Client] Connection suscessfully established with %s" %(nodeIP))

	def endCon(self):
		'''Signals end of communication with distant host'''
		self.SK.shutdown(socket.SHUT_WR)
		self.SK.close()
		print("[Client] Ended communication client side")

	def newReq(self):
		'''Declares self as a new node entering the network'''
		print("Making 1st contact")
		self.SK.send(str.encode("NODE NEW")) #New node declaration
		print("[Client] Signaled self")

	def consReq(self):
		'''Signals an onging consensus to other nodes'''
		print("Asking for consensus")	
		self.SK.send(str.encode("NODE CONSENSUS")) #Consensus request
		print("[Client] Signaled consensus")

	def memReq(self):
		'''Shares a new transaction with the other nodes'''
		print("Offering mempool update")
		self.SK.send(str.encode("NODE MEMUP")) #Mempool update request
		#SK.send(str.encode("PyObject0"))
		print("[Client] Shared new transaction")

	def getBC(self):
		'''Gets Blockchain from distant host'''
		self.SK.send("NODE BLOCKCHAIN")
		print("Asking for Blockchain")

	def shutNode(self):
		'''[DEBUG ONLY] Shuts distant host server down'''
		print("Shutting down the other node")
		self.SK.send(str.encode("NODE SHUTDOWN"))
		print("[Client] Distant node shut down")