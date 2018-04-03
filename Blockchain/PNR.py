class PNR(object):
	"""docstring for PNR"""
	def __init__(self, Id, name, firstname, phone, company, departure, arrival):
		super(PNR, self).__init__()
		self.Id = Id
		self.name = name
		self.firstname = firstname
		self.phone = phone
		self.company = company
		self.departure = departure
		self.arrival = arrival

	def __str__(self):
		return "PNR #{}".format(self.Id)

	def raw_data(self):
		return (str(self.Id) + str(self.name) + str(self.firstname) + str(self.phone) \
		       + str(self.company) + str(self.departure) + str(self.arrival))
