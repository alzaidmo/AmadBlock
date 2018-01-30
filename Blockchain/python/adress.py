# coding: utf-8

class Adress(object):
	def __init__(self, number, street, city, zipcode, country):
		super(Adress, self).__init__()
		self.number = number
		self.street = street
		self.city = city
		self.zipcode = zipcode
		self.country = country
		