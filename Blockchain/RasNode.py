# coding=utf-8

import Node
import PNR

if __name__ == "__main__":
	
	myNode = Node.Node("Raspberry Node")
	myNode.bootNode()

	myNode.client.conToNode("192.168.11.23", 4242)
	myNode.client.newReq()

	myNode.client.conToNode("192.168.11.23", 4242)
	myPNR = PNR.PNR("01000245", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")
	myNode.client.memReq(myPNR)

	myNode.client.conToNode("192.168.11.23", 4242)
	myPNR = PNR.PNR("01000246", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")
	myNode.client.memReq(myPNR)
	myNode.client.conToNode("192.168.11.23", 4242)
	myPNR = PNR.PNR("01000247", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")
	myNode.client.memReq(myPNR)
	myNode.client.conToNode("192.168.11.23", 4242)
	myPNR = PNR.PNR("01000248", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")
	myNode.client.memReq(myPNR)