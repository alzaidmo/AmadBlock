# coding: utf-8

import hashlib

class Block(object):
	"""
		Classe Block: Contient les attributs suivants :
						numero : Le numéro du block.
						hash : Le hash du block, permettant la vérification de la chaine.
						hash_previous : Le hash du block précedent dans la chaine.
						data : Les données contenues dans le block.
	"""
#_______________________________________________________________________
	# Constructeur
#_______________________________________________________________________	

	def __init__(self, num_=0, data_="",hashb_=None,hashp_=None):
		self.num = num_
		self.data = data_
		self.hashb = hashb_
		self.hash_previous = hashp_ 


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


#_______________________________________________________________________	
	# Autres méthodes
#_______________________________________________________________________	

	def addData(self, PNR):
		self.data = self.data + PNR

	def createHash(self):
		h = hashlib.sha224()
		info = self.data
		h.update(info.encode())
		self.hashb = h.hexdigest()


#_______________________________________________________________________	
	# Main loop
#_______________________________________________________________________	

def main():
	pass

if __name__ == '__main__':
	main()