# coding=utf-8

import Node
import time

sender_IP = "192.168.11.209"
#node_IP = "192.168.11.23" #IP of established node

if __name__ == "__main__":
	
	myNode = Node.Node("Primary Node")
	myNode.webHosts.add(sender_IP)
	#myNode.hosts.add(node_IP)
	myNode.bootNode()