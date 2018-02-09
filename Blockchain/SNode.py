# coding=utf-8

import Node

if __name__ == "__main__":
	
	myNode = Node.Node("Support", 4243)
	myNode.bootNode()

	myNode.startClient()
	myNode.client.conToNode("localhost", 4242)
	myNode.client.shutNode()