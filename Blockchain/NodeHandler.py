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
		print("["+GRN+"Handler"+RST+"] Starting a new request handler for {}\n".format(self.addr[0]))

		Req = bytes.decode(self.sock.recv(self.buffSize))

		if ((self.addr[0] not in self.node.hosts) & (Req != "NEW")):
			print("["+GRN+"Handler"+RST+"] Unkown host attempting to connect - Refusing\n")
			self.sock.send(b'0')  #Refusing unknown hosts

		else:
			print("["+GRN+"Handler"+RST+"] Connection established with %s on port %d" %(self.addr[0], self.addr[1]))

			if Req == "NEW":
				self.addNode()
				self.sock.send(b'1') # Confirm successfull treatment of the request					
			elif Req == "CONSENSUS":
				self.consent()
				self.sock.send(b'1')
			elif Req == "UPMEM":
				self.sock.send(b'1')
				self.updateMem()
			elif Req == "BLOCKCHAIN":
				self.sendBC()
#					elif Req == "SHUTDOWN":
#						self.shutNode(self.sock)

		
		self.sock.shutdown(socket.SHUT_RDWR)
		self.sock.close()
		
		print("["+GRN+"Handler"+RST+"] Succesfully processed {} request from {}\n".format(Req, self.addr[0]))


	def addNode(self):
		'''Add an incoming node to the list of trusted hosts'''
		print("["+GRN+"Handler"+RST+"] New node reaching out...")
		self.node.hosts.add(self.addr[0])
		print("["+GRN+"Handler"+RST+"] Added distant host to known hosts: {}".format(self.node.hosts))

	
	def consent(self):
		'''Trigger consesus'''
		print("["+GRN+"Handler"+RST+"] Consensus signaled by distant host")
		#self.node.consenter.consent()


	def updateMem(self):
		'''Update Mempool of current node'''
		print("["+GRN+"Handler"+RST+"] New transaction shared by distant host")
		data = self.sock.recv(1)
		transaction= b''
		while data:
			transaction += data
			data = self.sock.recv(1)

		transaction = pickle.loads(transaction)
		self.node.mempool.add(transaction)
		print("["+GRN+"Handler"+RST+"] Updated Mempool: {}".format(self.node.mempool))


	def sendBC(self):
		'''Send node's BC to distant host'''
		print("["+GRN+"Handler"+RST+"] Sending our BC to distant host")
		chain_b = pickle.dumps(self.node.blockchain)
		self.sock.send(chain_b)
		print("["+GRN+"Handler"+RST+"] BC sent")


#	def shutNode(self, self.sock):
#		'''Shuts the current node'''
#		print("["+GRN+"Handler"+RST+"] Distant host shutting down node...")
#		self.sock.send(b'1')
#		self.sock.shutdown(socket.SHUT_RDWR)
#		self.sock.close()
#		self.SKL.shutdown(socket.SHUT_RDWR)
#		self.SKL.close()
#		print("["+GRN+"Handler"+RST+"] Node shut down\n")

		