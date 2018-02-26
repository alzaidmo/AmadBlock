import Node

if __name__ == "__main__":
	
	myNode = Node.Node("DoS Node ~~(8:>", 4243)
	myNode.bootNode()

	myNode.client.conToNode("localhost", 4242)
	myNode.client.newReq()	

	while(True):
		myNode.client.conToNode("localhost", 4242)
		myNode.client.getBC()
		myNode.client.conToNode("localhost", 4242)
		myNode.client.memReq("DoS <-> DoS")