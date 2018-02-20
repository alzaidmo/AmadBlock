# coding=utf-8

import ServerThread
import Client

class Node(object):
	"""Initializing a Node"""
	def __init__(self, name, port):
		super(Node, self).__init__()
		self.name = name
		self.port = port
		self.mempool = set([])
		self.blockchain = ["Hello", "Amadeus rocks!"]
		self.server = ServerThread.ServerThread(self.name, self.port, self)
		self.client = 0
		self.miner = 0
		self.consenter = 0
	
	def bootNode(self):
		self.server.start()

	def startClient(self):
		self.client = Client.Client()