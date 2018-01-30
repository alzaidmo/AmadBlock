# coding=utf-8

import socket
import sys

class Client(object):
	"""Client part of the node responsible for sending inter-node requests"""
	def __init__(self):
		self.SK = 0  #Inter-node communication socket
		

	def comToNode(self, nodeIP, nodePort, request):
		'''Connects to Node at nodeIP on port nodePort'''
		
		self.SK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.SK.connect((nodeIP, nodePort))
		print("[OK] Connection suscessfully established with %s" %(nodeIP))
		request()
		print("[OK] Request suscessfully sent to %s" %(nodeIP))


	def endCom(self):
		self.SK.shutdown(socket.SHUT_RDWR)
		self.SK.close()

	def newReq(self):
		print("Making 1st contact")
		self.SK.send(str.encode("NODE NEW")) #New node declaration

	def consReq(self):
		print("Asking for consensus")	
		self.SK.send(str.encode("NODE CONSENSUS")) #Consensus request
		
	def memReq(self):
		print("Offering mempool update")
		self.SK.send(str.encode("NODE MEMUP")) #Mempool update request
		#SK.send(str.encode("PyObject0"))

	def shutNode(self):
		print("Shutting down the other node")
		self.SK.send(str.encode("NODE SHUTDOWN"))



if __name__ == "__main__":

	myClient = Client()
	myClient.comToNode('127.0.0.1', 4242, myClient.newReq)
	myClient.comToNode('127.0.0.1', 4242, myClient.consReq)
	myClient.comToNode('127.0.0.1', 4242, myClient.memReq)
	myClient.comToNode('127.0.0.1', 4242, myClient.shutNode)