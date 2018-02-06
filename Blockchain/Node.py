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
	def __init__(self, name, destIP, destPort):
		super(ClientThread, self).__init__()
		self.name = name
		self.destPort = destPort
		self.destIP = destIP

	def run(self):
		print("Starting " + self.name)
		myClient = Client.Client()
		myClient.comToNode(self.destIP, self.destPort, myClient.newReq)
		myClient.comToNode(self.destIP, self.destPort, myClient.consReq)
		myClient.comToNode(self.destIP, self.destPort, myClient.memReq)
		myClient.comToNode(self.destIP, self.destPort, myClient.shutNode)


if __name__ == "__main__":

	#Creating threads

	Server1 = ServThread("Server-1", 4242)
	Client1 = ClientThread("Client-1", "127.0.0.1", 4242)

	#Launching threads

	Server1.start()
	Client1.start()

	Server1.join()
	Client1.join()

	print("End of Node program")