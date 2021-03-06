# coding=utf-8

import socket
import WebHandler
import threading

BLU = "\u001b[34;1m"
RST = "\u001b[0m"

class WebServer(threading.Thread):
	"""WebServer type thread"""
	def __init__(self, name, port, node):
		super(WebServer, self).__init__()
		self.name = name
		self.port = port
		self.node = node
		self.queue = 3
		self.SKL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ifServ = '0.0.0.0'
		self.portServ = port

	
	def run(self):
		
		self.SKL.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.SKL.bind((self.ifServ, self.portServ))
		self.SKL.listen(self.queue)

		print("["+BLU+"WebServer"+RST+"] Node initialized, listening on port %d" %(self.portServ))
		
		while (True):
			print("["+BLU+"WebServer"+RST+"] Waiting for incoming connection...\n")
			(SKS, Add) = self.SKL.accept()
			SKS.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

			Handler = WebHandler.WebHandler(Add, SKS, self.node)
			Handler.start()