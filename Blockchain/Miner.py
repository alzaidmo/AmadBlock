# coding=utf-8

import Block
import Consenter

YLW = "\u001b[93;1m"
RST = "\u001b[0m"

class Miner(object):
	"""docstring for Miner"""
	def __init__(self, node, difficulty):
		super(Miner, self).__init__()
		self.node = node
		self.difficulty = difficulty# number of zeros in the hash
		
	def start(self):
		Miner.log("Starting mining...")
		self.createBlock()
		Miner.log("Mining done !")

	def createBlock(self):
		'''Initialises a new block and starts the proof of work'''

		transactionCount = len(self.node.mempool)
		Miner.log("{} transaction(s) in the mempool", transactionCount)

		data = ""
		for transaction in self.node.mempool:
			data = data + transaction

		lastBlock = self.node.blockchain[-1]

		block = Block.Block(num_ = len(self.node.blockchain), data_ = data, hashp_ = lastBlock.getHashb(), transactionCount = transactionCount)

		self.proofOfWork(block)

	def proofOfWork(self, block):
		'''Computes block's hash based on the difficulty and adds the new block to the blockchain'''

		Miner.log("Computing hash for the new block...")

		while ( block.getHashb()[:self.difficulty] != self.difficulty*"0" ):
			block.setNonce(block.getNonce() + 1)
			block.createHash();

		self.node.blockchain.append(block)
		Miner.log("Done computing, block successfuly added to the local blockchain !")

		self.node.mempool = set([])
		Miner.log("Flushed mempool !")

		self.node.consenter.consent()


	@staticmethod
	def log(msg, *params):
		''' logs a message to the screen '''
		if ( len(params) == 0 ):
			print("["+YLW+"Miner"+RST+"] " + msg + "\n")
		else:
			print(("["+YLW+"Miner"+RST+"] " + msg + "\n").format(*params))
