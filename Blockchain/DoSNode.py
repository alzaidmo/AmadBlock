import Node
import PNR

if __name__ == "__main__":
	
	myNode = Node.Node("DoS Node ~~(8:>")
	myNode.bootNode()

	myNode.client.conToNode("localhost", 4242)
	myNode.client.newReq()	

	DoSPNR = PNR.PNR(("0424242", "~~(8:>", "DoS", "0612485674", "Air India", "CDG", "JFK"))

	while(True):
		myNode.client.conToNode("localhost", 4242)
		myNode.client.getBC()
		myNode.client.conToNode("localhost", 4242)
		myNode.client.memReq(DoSPNR)