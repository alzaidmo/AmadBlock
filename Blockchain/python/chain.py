# coding: utf-8
from block import *

class Chain(object):
	"""
		Classe Chain: Contient les attributs suivants :
				
	"""

#_______________________________________________________________________
	# Constructeur
#_______________________________________________________________________
	def __init__(self, b0=None, blocks=[]):
		self.b0 = b0
		self.blocks = blocks

#_______________________________________________________________________	
	# Getters et Setters
#_______________________________________________________________________

	def getB0(self):
		""" 
			Getter de b0
			@Entrée : Aucune
			@Sortie : Attribut b0 
		"""
		return(self.b0)
	
	def getBlocks(self):
		""" 
			Getter de blocks
			@Entrée : Aucune
			@Sortie : Attribut blocks 
		"""
		return(self.blocks)
	
	def setB0(self, b0):
		"""
			Setter de b0
			@Entrée : Un objet de type Block
			@Sortie : Aucune
		"""
		self.b0 = b0

#_______________________________________________________________________	
	# Autres méthodes
#_______________________________________________________________________	

	def addBlock(self, bk):
		"""
			Fonction permettant d'ajouter un block dans l'attribut blocks.
			@Entrée : un objet de type block
			@Sortie : Aucune
		"""
		self.blocks.append(bk)

#_______________________________________________________________________	
	# Fonctions externes
#_______________________________________________________________________	


def initialize():
	""" 
		Fonction qui permet d'initialiser une BlockChain
		@Entrée : Aucune
		@Sortie : Un objet de type Chain 
	"""
	c = Chain()
	b0 = Block()
	b0.addData("Block Initial")
	b0.createHash()
	c.setB0(b0)
	c.addBlock(b0)
	return(c)

#_______________________________________________________________________	
	# Main loop
#_______________________________________________________________________	

def main():
	#_________________
		# Ce block vérifie que b0 est le premier block de la liste de block dans l'attribut blocks
	chaine = initialize()
	n1 = chaine.getB0().getNum()
	n2 = chaine.getBlocks()[0].getNum()
	d1 = chaine.getB0().getData()
	d2 = chaine.getBlocks()[0].getData()
	h1 = chaine.getB0().getHashb()
	h2 = chaine.getBlocks()[0].getHashb()
	hp1 = chaine.getB0().getHashPrev()
	hp2 = chaine.getBlocks()[0].getHashPrev()
	print("Vérification")
	print("Numéro :", n1, n2)
	print("Data :", d1, d2)
	print("Hash :", h1, h2)
	print("Hash précédent :", hp1, hp2)

	if n1==n2 and d1==d2 and h1==h2 and hp1==hp2:
		print("Egalité complète :", True)
	else:
		print("Egalité complète :", False)
		print("b0 n'est pas le premier block")
	#_________________
	chaine.addBlock(Block(1,"block de test 1"))
	print(chaine.getBlocks()[1].getNum())
		

if __name__ == '__main__':
	main()