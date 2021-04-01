class parent:
	def __init__(self, a=1, b=0):
		self.a = a
		self.b = b
	def pr(self):
		print(self.a)

class child(parent):
	def me(self):
		print(a)
#	print(a) -- this doesn't work, a lone print statement, not in a method

p = child(5, 4)
q = child(7)
z = child()

w = parent(3, 6)


print(p.a) # prints 5
print(q.b) # prints 0
print(z.a) # prints 1
