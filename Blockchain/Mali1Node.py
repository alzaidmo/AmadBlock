# coding=utf-8

import Node
import time
import Miner
import Client
import Block

sender_IP = "127.0.0.1" #IP of the web server from which requests are emanating
node_IP = "192.168.11.23" #IP of established node

class MaliciousMiner(Miner.Miner):
	def __init__(self, node, difficulty):
		super(MaliciousMiner, self).__init__(node, difficulty)
		self.node = node
		self.client = Client.Client("Miner")
		self.difficulty = difficulty# number of zeros in the hash
		
		
	def createBlock(self):
		transactionCount = len(self.node.mempool)
		data = []

		if transactionCount != 0:
			self.log("{} transaction(s) in the mempool", transactionCount)
			for transaction in self.node.mempool:
				data.append(transaction.raw_data())
			self.node.mempool = set([])
			self.log("Flushed mempool !\n")

			lastBlock = self.node.blockchain[-1]

			block = Block.Block(num_ = len(self.node.blockchain), data_ = data, hashp_ = lastBlock.getHashb(), transactionCount = transactionCount)

			self.proofOfWork(block)

	def proofOfWork(self, block):
		'''Computes block's hash based on the difficulty and adds the new block to the blockchain'''

		self.log("Computing hash for the new block")
		prev_nonce = self.node.blockchain[-1].getNonce()
		self.log("Solving proof of work: hash of ({} + myHash) starts with {} zeros...", prev_nonce, self.difficulty)

		#while ( block.getProof()[:self.difficulty] != self.difficulty*"0" ):
		#	block.setNonce(block.getNonce() + 1)
		#	block.setProof(block.createPoW(prev_nonce));

		block.setHash(block.createHash()); #Generate the hash of the block once the nonce has been fixed

		#Blockchain might have been replaced during mining, to avoid duplicate blocks, check if the freshly mined block still fits in the updated Blockchain
		
		if self.blockInOrder(block):
		
			self.node.blockchain.append(block)
			self.log("Block#{} has been mined\n\t- nonce: {}\n\t- Proof of work: {}\n\t- Previous hash: {}\n\t- Block hash: {}\n", \
		        block.getNum(), block.getNonce(), block.getProof(), block.getHashPrev(), block.getHashb())

			for host in self.node.hosts:
				self.client.conToNode(host, 4242)
				self.client.consReq()
			self.node.consenter.consent()


	def blockInOrder(self, new_block):
		"""
		Determine if a newly created block can be added to the current Blockchain
		before asking for consensus

		:param block: A block
		:return: True if valid, False if not
		"""

		last_block = self.node.blockchain[-1]

		# Check that the block is at the right place
		calc_prevHash = last_block.createHash()
		if new_block.getHashPrev() != calc_prevHash:
			self.log("Abort linking of the new block - The newly created block does not belong behind the last block of the current Blockchain\n\t"+
			"Maybe the blockchain was updated during mining")
			return False
		
		return True


if __name__ == "__main__":
	
	myMaliciousNode = Node.Node("Malicious Node")
	myMaliciousNode.miner = MaliciousMiner(myMaliciousNode, myMaliciousNode.difficulty)
	myMaliciousNode.webHosts.add(sender_IP)
	myMaliciousNode.hosts.add(node_IP)
	myMaliciousNode.bootNode()

	for node in myMaliciousNode.hosts:
		myMaliciousNode.client.conToNode(node, 4242)
		myMaliciousNode.client.newReq()