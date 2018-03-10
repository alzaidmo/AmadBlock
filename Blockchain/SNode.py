# coding=utf-8

import Node
import PNR

if __name__ == "__main__":
	
	myNode = Node.Node("Secondary Node")
	myNode.bootNode()

	myNode.client.conToNode("localhost", 4242)
	myNode.client.newReq()
	myNode.client.conToNode("localhost", 4242)
	myNode.client.getBC()
	myNode.client.conToNode("localhost", 4242)
	myPNR = PNR.PNR("01000245", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")
	myNode.client.memReq(myPNR)