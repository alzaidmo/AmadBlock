# coding=utf-8

import Node
import time

sender_IP = "172.20.15.83"

if __name__ == "__main__":
	
	myNode = Node.Node("Primary Node")
	myNode.webHosts.add(sender_IP)
	myNode.bootNode()
