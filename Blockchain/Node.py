# coding=utf-8

import NodeServer
import WebServer
import Client
import Block
import Miner
import Consenter
import pickle

class Node(object):
	"""Initializing a Node"""
	def __init__(self, name):
		super(Node, self).__init__()
		self.name = name
		self.mempool = set([])
		self.blockchain = [Block.Block(num_ = 0, data_ = ["Genesis Block"], hashb_ = "None", hashp_ = "None", transactionCount = 1)]
		self.difficulty = 4 
		self.nodeServer = NodeServer.NodeServer(name, 4242, self)
		self.webServer = WebServer.WebServer(name, 4254, self)
		self.client = Client.Client(name)
		self.miner = Miner.Miner(self, self.difficulty)
		self.consenter = Consenter.Consenter(self, self.difficulty)
		self.hosts = set([])
		self.webHosts = set([])
	
	def bootNode(self):
		'''Start the listening server (thread)'''

		self.loadBC()
		self.nodeServer.start()
		self.webServer.start()

		self.miner.start() #Start mining

	def loadBC(self):
		try:
		#If a file already exists
			self.blockchain = pickle.load(open("./"+self.name+".bc", "rb"))
		except EOFError:
		#If the file is empty, store genesis block to start with
			self.saveBC()

	def saveBC(self):
		pickle.dump(self.blockchain, open("./"+self.name+".bc", "wb"))
