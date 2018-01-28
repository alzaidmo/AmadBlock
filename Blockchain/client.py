import socket
import sys



def linkToNode(nodeIP, request):
	'''Connects to Node at nodeIP'''
	SK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	IPServ = nodeIP
	PortServ = 4242
	BuffSize = 128

	SK.connect((IPServ, PortServ))
	
	request(SK)

	#data = SK.recv(BuffSize) #Read server echo
	#print("Server >>>", bytes.decode(data))

	SK.shutdown(socket.SHUT_RDWR)
	SK.close()

	print("End of connection")



def newReq(SK):
	print("Making 1st contact")
	SK.send(str.encode("NODE NEW")) #New node declaration

def consReq(SK):
	print("Asking for consensus")	
	SK.send(str.encode("NODE CONSENSUS")) #Consensus request
	
def memReq(SK):
	print("Offering mempool update")
	SK.send(str.encode("NODE MEMUP")) #Mempool update request
	SK.send(str.encode("PyObject0"))

def shutNode(SK):
	print("Shutting down the other node")
	SK.send(str.encode("NODE SHUTDOWN"))



if __name__ == "__main__":
	
	linkToNode('127.0.0.1', newReq)
	linkToNode('127.0.0.1', shutNode)