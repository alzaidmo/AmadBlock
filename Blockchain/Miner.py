# coding=utf-8

import Block
import Consenter
import threading
import PNR
import Client

YLW = "\u001b[93;1m"
RST = "\u001b[0m"

class Miner(threading.Thread):
	"""docstring for Miner"""
	def __init__(self, node, difficulty):
		super(Miner, self).__init__()
		self.node = node
		self.client = Client.Client("Miner")
		self.difficulty = difficulty# number of zeros in the hash
		
	def run(self):
		while True:
			self.createBlock()

	def createBlock(self):
		'''Initialises a new block and starts the proof of work'''

		transactionCount = len(self.node.mempool) # transactions to process
		data = []

		if transactionCount != 0:
			Miner.log("{} transaction(s) in the mempool", transactionCount)
			for i in range(transactionCount):
				data.append(self.node.mempool[i].raw_data())

			# deleting what was processed from the mempool => keeping what was received for the next session
			self.node.mempool = self.node.mempool[transactionCount:]

			Miner.log("{} transaction(s) received for the next mining ", len(self.node.mempool))

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
			block.setProof(block.createPoW(prev_nonce));

		block.setHash(block.createHash()); #Generate the hash of the block once the nonce has been fixed
		

		#Blockchain might have been replaced during mining, to avoid duplicate blocks, check if the freshly mined block still fits in the updated Blockchain
		
		if self.blockInOrder(block):
		
			self.node.blockchain.append(block)
			Miner.log("Block#{} has been mined\n\t- nonce: {}\n\t- Proof of work: {}\n\t- Previous hash: {}\n\t- Block hash: {}\n", \
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



	@staticmethod
	def log(msg, *params):
		''' logs a message to the screen '''
		if ( len(params) == 0 ):
			print("["+YLW+"Miner"+RST+"] " + msg)
		else:
			print(("["+YLW+"Miner"+RST+"] " + msg).format(*params))
