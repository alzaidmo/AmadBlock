RED = "\u001b[31;1m"
RST = "\u001b[0m"

class Consenter(object):
	"""docstring for Consenter"""
	def __init__(self, node, difficulty):
		super(Consenter, self).__init__()
		self.node = node
		self.difficulty = difficulty# number of zeros in the hash

	def consent(self):
		Consenter.log("Resolving blockchain conflicts")
		replaced = self.resolveConflicts()

		if replaced:
			
			Consenter.log("Blockchain was replaced")
			pass
			#Our chain was replaced
		else:
			"""for node in self.node.hosts:
				self.node.client.conToNode(node, 4242)
				self.node.client.consReq()"""
			Consenter.log("Blockchain is authoritative")
			pass
			#Our chain is authoritative
		for block in self.node.blockchain:
			Consenter.log("Current Blockchain {}", block)
		print("\n")


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
			self.node.client.conToNode(node, 4242)
			chain = self.node.client.getBC()
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
			# Check that the hash of the block is correct
			if block.getHashPrev() != last_block.getHashb():
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
		if(lastBlock.getHashb() != block.getHashPrev() or block.getHashb()[:self.difficulty] != self.difficulty*"0"):
			return False

		return True
		

	@staticmethod
	def log(msg, *params):
		''' logs a message to the screen '''
		if ( len(params) == 0 ):
			print("["+RED+"Consenter"+RST+"] " + msg)
		else:
			print(("["+RED+"Consenter"+RST+"] " + msg).format(*params))
