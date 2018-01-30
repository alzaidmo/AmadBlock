# coding=utf-8

import Client
import Server

import threading

class ServThread(threading.Thread):
	"""Server type thread"""
	def __init__(self, name, port):
		super(ServThread, self).__init__()
		self.name = name
		self.port = port

	def run(self):
		print("Starting " + self.name)
		myServer = Server.Server(self.port)
		myServer.startNode()
		myServer.acceptReq()		


class ClientThread(threading.Thread):
	"""Server type thread"""
	def __init__(self, name, nodePort):
		super(ClientThread, self).__init__()
		self.name = name
		self.nodePort = nodePort

	def run(self):
		print("Starting " + self.name)
		myClient = Client.Client()
		myClient.comToNode('127.0.0.1', self.nodePort, myClient.newReq)
		myClient.comToNode('127.0.0.1', self.nodePort, myClient.consReq)
		myClient.comToNode('127.0.0.1', self.nodePort, myClient.memReq)
		myClient.comToNode('127.0.0.1', self.nodePort, myClient.shutNode)


if __name__ == "__main__":

	#Creating threads

	Server1 = ServThread("Server-1", 4242)
	Server2 = ServThread("Server-2", 4343)

	Client1 = ClientThread("Client-1", 4343)
	Client2 = ClientThread("Client-2", 4242)

	#Launching threads

	Server1.start()
	Server2.start()
	Client1.start()
	Client2.start()


	Server1.join()
	Server2.join()
	Client1.join()
	Client2.join()

	print("End of Node program")