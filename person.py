import human
import time

class person(human.human):
	'''create a person object with his name.
	And call SayHello will introduce himself.
	'''
	def SayHello(self):
		print "Hi! My name is " + str(self)

class shirley(person):

	def __init__(self):
		person.__init__(self, 'tainwan', 'shirley')

	def introduce(self):
		self.SayHello()
		time.sleep(2)
		print "I live in " + self.addr
		time.sleep(2)
		print 'My age is ' + str(self.age)
			
