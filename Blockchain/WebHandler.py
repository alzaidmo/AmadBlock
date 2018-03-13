# coding=utf-8

import threading
import pickle
import socket

GRN = "\u001b[32;1m"
RST = "\u001b[0m"

class NodeHandler(threading.Thread):
	"""docstring for NodeHandler"""
	def __init__(self, addr, sock, node):
		super(NodeHandler, self).__init__()
		self.addr = addr
		self.sock = sock
		self.node = node
		self.buffSize = 32

	def run(self):
		print("["+GRN+"Handler"+RST+"] Starting a new request handler for {}".format(self.addr[0]))

		data = bytes.decode(self.sock.recv(self.buffSize))
		typeReq, Req = data.split(' ')[0], data.split(' ')[1] #Splitting request

		if ((self.addr[0] not in self.node.hosts) & (Req != "NEW")):
			print("["+GRN+"Handler"+RST+"] Unkown host attempting to connect - Refusing\n")
			self.sock.send(b'0')  #Refusing unknown hosts

		else:
			print("["+GRN+"Handler"+RST+"] Connection established with %s on port %d" %(self.addr[0], self.addr[1]))

			self.sock.send(b'1')
			self.addToMem()

		
		self.sock.shutdown(socket.SHUT_RDWR)
		self.sock.close()
		
		print("["+GRN+"Handler"+RST+"] Succesfully processed {} request from {}\n".format(Req, self.addr[0]))



	def addToMem(self):
		'''Update Mempool of current node'''
		print("["+GRN+"Handler"+RST+"] New transaction incoming from Web client")
		data = self.sock.recv(1)
		transaction= b''
		while data:
			transaction += data
			data = self.sock.recv(1)

		transaction = pickle.loads(transaction)
		self.node.mempool.add(transaction)
		print("["+GRN+"Handler"+RST+"] Updated Mempool: {}".format(self.node.mempool))