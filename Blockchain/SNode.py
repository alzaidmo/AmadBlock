# coding=utf-8

import Node

if __name__ == "__main__":
	
	myNode = Node.Node("Secondary Node", 4243)
	myNode.bootNode()

	myNode.client.conToNode("localhost", 4242)
	myNode.client.newReq()
	myNode.client.conToNode("localhost", 4242)
	myNode.client.getBC()
	myNode.client.conToNode("localhost", 4242)
	myNode.client.memReq("CDG <-> MNL")