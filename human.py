class human:
	name = 'no name'
	age = 0
	healthy = 100
	addr = 'heaven'
	def __init__(self, place):
		self.addr = place

	def __init__(self, place, name):
		self.addr = place
		self.name = name

	def __str__(self):
		return self.name

class man(human):
	sex = 'XY'

class woman(human):
	sex = 'XX'


