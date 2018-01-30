# coding: utf-8
import adress

class Agency(object):
	"""docstring for Agency"""
	def __init__(self, name, siret):
		super(Agency, self).__init__()
		self.name = name
		self.siret = siret
		self.adress = adress.Adress()
