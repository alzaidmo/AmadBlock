# coding=utf-8

import Block
import Consenter
import threading

YLW = "\u001b[93;1m"
RST = "\u001b[0m"

class Miner(threading.Thread):
	"""docstring for Miner"""
	def __init__(self, node, difficulty):
		super(Miner, self).__init__()
		self.node = node
		self.difficulty = difficulty# number of zeros in the hash
		
	def run(self):
		while True:
			self.createBlock()

	def createBlock(self):
		'''Initialises a new block and starts the proof of work'''

		transactionCount = len(self.node.mempool)
		data = []

		if transactionCount != 0:
			Miner.log("{} transaction(s) in the mempool", transactionCount)
			for transaction in self.node.mempool:
				data.append(transaction)
			self.node.mempool = set([])
			Miner.log("Flushed mempool !\n")

			lastBlock = self.node.blockchain[-1]

			block = Block.Block(num_ = len(self.node.blockchain), data_ = data, hashp_ = lastBlock.getHashb(), transactionCount = transactionCount)

			self.proofOfWork(block)

	def proofOfWork(self, block):
		'''Computes block's hash based on the difficulty and adds the new block to the blockchain'''

		Miner.log("Computing hash for the new block")
		prev_nonce = self.node.blockchain[-1].getNonce()
		Miner.log("Solving proof of work: hash of ({} + myHash) starts with {} zeros...", prev_nonce, self.difficulty)

		while ( block.getProof()[:self.difficulty] != self.difficulty*"0" ):
			block.setNonce(block.getNonce() + 1)
			block.createPoW(prev_nonce);

		block.createHash(); #Generate the hash of the block once the nonce has been fixed

		self.node.blockchain.append(block)
		Miner.log("Done computing, nonce {} / PoW {} - Block#{} has been mined", block.getNonce(), block.getProof(), block.getNum())

		for host in self.node.hosts:
			self.node.client.conToNode(host, 4242)
			self.node.client.consReq()
		self.node.consenter.consent()


	@staticmethod
	def log(msg, *params):
		''' logs a message to the screen '''
		if ( len(params) == 0 ):
			print("["+YLW+"Miner"+RST+"] " + msg)
		else:
			print(("["+YLW+"Miner"+RST+"] " + msg).format(*params))
