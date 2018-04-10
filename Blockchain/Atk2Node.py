# coding=utf-8

import Node
import time
import Block

sender_IP = "127.0.0.1" #IP of the web server from which requests are emanating
#node_IP = "172.20.15.83" #IP of established node

if __name__ == "__main__":
	
	customBlock = Block.Block('2', "X")

	myNode = Node.Node("Malicious Node")
	myNode.webHosts.add(sender_IP)
	#myNode.hosts.add(node_IP)
	myNode.bootNode()

	for node in myNode.hosts:
		myNode.client.conToNode(node, 4242)
		myNode.client.newReq()
	#Declare onself to established nodes

	time.sleep(5)
	print("Inserting faulty block")
	myNode.blockchain[2] = customBlock