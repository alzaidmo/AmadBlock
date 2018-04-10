import Node
import PNR

if __name__ == "__main__":
	
	myNode = Node.Node("Web Server")

	myNode.client.conToNode("localhost", 4242)
	myNode.client.newReq()	

	PNR1 = PNR.PNR("1", "~~(8:>", "DoS", "0612485674", "Air India", "CDG", "JFK")
	PNR2 = PNR.PNR("2", "~~(8:>", "DoS", "0612485674", "Air India", "CDG", "JFK")
	PNR3 = PNR.PNR("3", "~~(8:>", "DoS", "0612485674", "Air India", "CDG", "JFK")
	PNR4 = PNR.PNR("4", "~~(8:>", "DoS", "0612485674", "Air India", "CDG", "JFK")


	myNode.client.conToNode("localhost", 4254)
	myNode.client.webTrans(PNR1)
	myNode.client.conToNode("localhost", 4254)
	myNode.client.webTrans(PNR2)
	myNode.client.conToNode("localhost", 4254)
	myNode.client.webTrans(PNR3)
	myNode.client.conToNode("localhost", 4254)
	myNode.client.webTrans(PNR4)