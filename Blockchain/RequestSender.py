# coding=utf-8

import Node
import PNR

nodes = ["172.20.15.83", "172.20.15.42"] #IPs of the nodes to which requests should be sent  

if __name__ == "__main__":
	
	myNode = Node.Node("Request Sender")

	myPNR1 = PNR.PNR("1", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")
	myPNR2 = PNR.PNR("2", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")
	myPNR3 = PNR.PNR("3", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")
	myPNR4 = PNR.PNR("4", "Oiragol", "Mathieu", "0612485674", "Air India", "CDG", "JFK")

	for host in nodes:
		myNode.client.conToNode(host, 4254)
		myNode.client.webTrans(myPNR1)

	for host in nodes:
		myNode.client.conToNode(host, 4254)
		myNode.client.webTrans(myPNR2)

	for host in nodes:
		myNode.client.conToNode(host, 4254)
		myNode.client.webTrans(myPNR3)

	for host in nodes:	
		myNode.client.conToNode(host, 4254)
		myNode.client.webTrans(myPNR4)
