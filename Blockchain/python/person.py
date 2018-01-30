# coding: utf-8
import adress

class Person(object):
	def __init__(self, fname, sname, phone, mail):
		self.fname = fname
		self.sname = sname
		self.phone = phone
		self.mail = mail
		self.adress = adress.Adress()

			