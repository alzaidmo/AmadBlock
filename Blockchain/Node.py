# coding=utf-8

import Server
import Client
import Block
import Miner
import Consenter

class Node(object):
	"""Initializing a Node"""
	def __init__(self, name, port):
		super(Node, self).__init__()
		self.name = name
		self.port = port
		self.mempool = set([])
		self.blockchain = [Block.Block(num_ = 0, data_ = "genesis block", hashb_ = "None", hashp_ = "None", transactionCount = 1)]
		self.difficulty = 4 
		self.server = Server.Server(name, port, self)
		self.client = Client.Client()
		self.miner = Miner.Miner(self, self.difficulty)
		self.consenter = Consenter.Consenter(self, self.difficulty)
		self.hosts = set([])
	
	def bootNode(self):
		'''Start the listening server (thread)'''
		self.server.start()
