# coding: utf-8

import hashlib
import time

class Block(object):
	"""
		Classe Block: Contient les attributs suivants :
						numero : Le numéro du block.
						hash : Le hash du block, permettant la vérification de la chaine.
						hash_previous : Le hash du block précedent dans la chaine.
						data : Les données contenues dans le block.
						transactionCount : Le nombre de transactions dans le block
	"""
#_______________________________________________________________________
	# Constructeur
#_______________________________________________________________________	

	def __init__(self, num_ = 0, data_ = "", hashb_ = None, hashp_ = None, transactionCount = 1):
		self.num = num_
		self.data = data_
		self.hashb = hashb_
		self.hash_previous = hashp_ 
		self.transactionCount = transactionCount
		self.timestamp = time.time()
		self.nonce = 0
		self.proof = 123456789


#_______________________________________________________________________	
	# Getters et Setters
#_______________________________________________________________________	

	def getNum(self):
		""" 
			Getter de numéro
			@Entrée : Aucune
			@Sortie : Attribut num 
		"""
		return(self.num)

	def getData(self):
		""" 
			Getter de data
			@Entrée : Aucune
			@Sortie : Attribut data 
		"""
		return(self.data)

	def getHashb(self):
		""" 
			Getter de hashb
			@Entrée : Aucune
			@Sortie : Attribut hashb 
		"""
		return(self.hashb)

	def getHashPrev(self):
		""" 
			Getter de hash_previous
			@Entrée : Aucune
			@Sortie : Attribut hash_previous 
		"""
		return(self.hash_previous)

	def getNonce(self):
		""" 
			Getter de nonce
			@Entrée : Aucune
			@Sortie : Attribut nonce 
		"""
		return(self.nonce)

	def getProof(self):
		""" 
			Getter de proof
			@Entrée : Aucune
			@Sortie : Attribut proof 
		"""
		return(str(self.proof))

	def getTimestamp(self):
		""" 
			Getter de timestamp
			@Entrée : Aucune
			@Sortie : Attribut timestamp 
		"""
		return(self.timestamp)

	def getTransactionCount(self):
		""" 
			Getter de transactionCount
			@Entrée : Aucune
			@Sortie : Attribut transactionCount 
		"""
		return(self.transactionCount)

	def setNum(self, nb):
		""" 
			Setter de num
			@Entrée : Un entier 
			@Sortie : Aucune
		"""
		self.num = nb

	def setHashPrev(self, hashpb):
		""" 
			Setter de hashpb
			@Entrée : Un hash 
			@Sortie : Aucune
		"""
		self.hash_previous = hashpb

	def setTimestamp(self, timestamp):
		""" 
			Setter de timestamp
			@Entrée : Un timestamp 
			@Sortie : Aucune
		"""
		self.timestamp = timestamp

	def setNonce(self, nonce):
		""" 
			Setter de nonce
			@Entrée : Un nonce 
			@Sortie : Aucune
		"""
		self.nonce = nonce

	def setTransactionCount(self, transactionCount):
		""" 
			Setter de transactionCount
			@Entrée : Un transactionCount 
			@Sortie : Aucune
		"""
		self.transactionCount = transactionCount


#_______________________________________________________________________	
	# Autres méthodes
#_______________________________________________________________________	

	def addData(self, PNR):
		self.data = self.data + PNR

	def createHash(self):
		h = hashlib.sha256()
		info = (str(self.num) + str(self.data) + str(self.hash_previous) + str(self.transactionCount) + str(self.timestamp) + str(self.nonce)).encode()
		h.update(info)
		self.hashb = h.hexdigest()

	def createPoW(self, prev_nonce):
		h = hashlib.sha256()
		info = (str(prev_nonce)+str(self.num) + str(self.data) + str(self.hash_previous) + str(self.transactionCount) + str(self.timestamp) + str(self.nonce)).encode()
		h.update(info)
		self.proof = h.hexdigest()

	def __str__(self):
		msg = "Block #{} - Transactions: ".format(self.num)
		for tx in self.data:
			msg += "{} ".format(tx)
		return msg