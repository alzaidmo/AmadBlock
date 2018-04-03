# coding=utf-8

import Node
import PNR

nodes = {} #IPs of the nodes to which requests should be sent

if __name__ == "__main__":
	
	myNode = Node.Node("Request Sender")

	myNode.client.conToNode("localhost", 4254)
	myPNR = PNR.PNR("01000245", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")
	myNode.client.webTrans(myPNR)

	myNode.client.conToNode("localhost", 4254)
	myPNR = PNR.PNR("01000246", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")
	myNode.client.webTrans(myPNR)
	myNode.client.conToNode("localhost", 4254)
	myPNR = PNR.PNR("01000247", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")
	myNode.client.webTrans(myPNR)
	myNode.client.conToNode("localhost", 4254)
	myPNR = PNR.PNR("01000248", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")
	myNode.client.webTrans(myPNR)