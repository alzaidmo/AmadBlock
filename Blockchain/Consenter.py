import hashlib
import Client

RED = "\u001b[31;1m"
RST = "\u001b[0m"

class Consenter(object):
	"""docstring for Consenter"""
	def __init__(self, node, difficulty):
		super(Consenter, self).__init__()
		self.node = node
		self.client = Client.Client("Consenter")
		self.difficulty = difficulty# number of zeros in the hash
		self.running = False #Is a consensus already running?

	def consent(self):
		if not (self.running):
			self.running = True
			Consenter.log("Resolving blockchain conflicts")
			replaced = self.resolveConflicts()

			if replaced:
				Consenter.log("Blockchain was replaced")
			else:
				Consenter.log("Blockchain is authoritative")
				
			#Clean mempool from processed transactions or in case of transaction redundancy 
			self.updateMempool()
			self.node.saveBC()
			self.running = False
			for block in self.node.blockchain:
				self.log("Current Blockchain {}", block)
			print("\n")
		else:
			self.log("A consensus is already running")


	def resolveConflicts(self):
		"""
		This is our consensus algorithm, it resolves conflicts
		by replacing our chain with the longest one in the network.

		:return: True if our chain was replaced, False if not
		"""

		neighbours = self.node.hosts
		new_chain = None

		# We're only looking for chains longer than ours
		max_length = len(self.node.blockchain)

		# Grab and verify the chains from all the nodes in our network
		for node in neighbours:
			self.client.conToNode(node, 4242)
			chain = self.client.getBC()
			if chain:
				length = len(chain)

			# Check if the length is longer and the chain is valid
			if length > max_length and self.isChainValid(chain):
				max_length = length
				new_chain = chain

		# Replace our chain if we discovered a new, valid chain longer than ours
		if new_chain:
			self.node.blockchain = new_chain
			return True

		return False


	def isChainValid(self, chain):
		"""
		Determine if a given blockchain is valid

		:param chain: A blockchain
		:return: True if valid, False if not
		"""

		last_block = chain[0]
		current_index = 1

		while current_index < len(chain):
			block = chain[current_index]
			# Check that the block is at the right place
			calc_prevHash = last_block.createHash()
			if block.getHashPrev() != calc_prevHash:
				self.log("Error in the block order\nAnnounced by Block#{}: {}\nCalculated from Block#{}: {}\nBlock #{} is corrupted", block.getNum(), block.getHashPrev(), last_block.getNum(), calc_prevHash, current_index - 1)
				return False

			# Check that the Proof of Work is correct
			if not self.isProofValid(last_block, block):
				return False

			last_block = block
			current_index += 1

		return True

	def isProofValid(self, lastBlock, block):
		"""
		Validates the Proof

		:param last_proof: lastblock
		:param proof: block
		:return: <bool> True if correct, False if not.

		"""
		prev_nonce = lastBlock.getNonce()
		calc_PoW = block.createPoW(prev_nonce)

		if (calc_PoW[:self.difficulty] != self.difficulty*"0"):
			self.log("Error in the proof of work\nCalculated: {}\nEither Block#{} has not generated a PoW or Block #{} is corrupted", calc_PoW, block.getNum(), lastBlock.getNum())
			return False

		return True

	def updateMempool(self):
		"""
		Cleans mempool from transactions that also appear in the blockchain that was received from other miners
		"""
		for block in self.node.blockchain:
			for blockTransaction in block.getData():
				for memTransaction in self.node.mempool:
					if self.computeHash(memTransaction.raw_data()) == self.computeHash(blockTransaction):
						self.node.mempool.remove(memTransaction)
						break


	def computeHash(self,data):
		"""
		Computes an md5 hash for the data
		:data : data to compute the md5 hash for
		:return : the md5 hash
		"""
		h = hashlib.md5()
		h.update(data)
		return h.hexdigest()

	@staticmethod
	def log(msg, *params):
		''' logs a message to the screen '''
		if ( len(params) == 0 ):
			print("["+RED+"Consenter"+RST+"] " + msg)
		else:
			print(("["+RED+"Consenter"+RST+"] " + msg).format(*params))
