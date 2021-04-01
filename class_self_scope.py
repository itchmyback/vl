class Aclass:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	# variables -- these are class variables
	# must instance variables go under __init__ ?
	a = 1
	b = 2
	c = 3

	def show(self):
		print("Super hello")

#	self.a = self.x # this is an error
	
	def run(self):
# 		print(a, b, c) # vars not defined, class scope not function scope
		myname = "John" # var  has function scope
		print(myname)
		print(Aclass.a)
		self.a = 7
		print(self.a) # declaring instance version of a, because the scope run() has reference to self
#		print(x) # x not defined

class Subclass(Aclass):
	def subShow(self):
#		show() # This won't work, must call as either Class method or instance method self.show()
		self.show()
		print("Sub hello")

ainstance = Aclass(4, 5, 6)
ainstance.run()

subinstance = Subclass(7, 8, 9)
subinstance.subShow()
