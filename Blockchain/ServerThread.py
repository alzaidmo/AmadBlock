# coding=utf-8

import Server

import threading

class ServerThread(threading.Thread):
	"""Server type thread"""
	def __init__(self, name, port, node):
		super(ServerThread, self).__init__()
		self.name = name
		self.port = port
		self.node = node

	def run(self):
		print("Starting " + self.name)
		myServer = Server.Server(self.port, self.node)
		myServer.startServer()
		myServer.treatReq()