# coding=utf-8

import Server
import Client

class Node(object):
	"""Initializing a Node"""
	def __init__(self, name, port):
		super(Node, self).__init__()
		self.name = name
		self.port = port
		self.mempool = set([])
		self.blockchain = ["Hello", "Amadeus rocks!"]
		self.server = Server.Server(name, port, self)
		self.client = Client.Client()
		self.miner = 0
		self.consenter = 0
		self.hosts = set([])
	
	def bootNode(self):
		'''Start the listening server (thread)'''
		self.server.start()