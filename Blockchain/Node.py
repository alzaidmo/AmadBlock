# coding=utf-8

import NodeServer
import WebServer
import Client

class Node(object):
	"""Initializing a Node"""
	def __init__(self, name):
		super(Node, self).__init__()
		self.name = name
		self.mempool = set([])
		self.blockchain = ["Block#0", "Block#1"]
		self.nodeServer = NodeServer.NodeServer(name, 4242, self)
		self.webServer = WebServer.WebServer(name, 4254, self)
		self.client = Client.Client()
		self.miner = 0
		self.consenter = 0
		self.hosts = set([])
	
	def bootNode(self):
		'''Start the listening server (thread)'''
		self.nodeServer.start()
		self.webServer.start()