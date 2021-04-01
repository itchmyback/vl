class Operand:
	def __init__(self, cond_type, cond_operator, cond_param, action_type, action_param):
		self.cond_type =  cond_type
		self.cond_operator = cond_operator  
		self.cond_param = cond_param 
		self.action_type = action_type 
		self.action_param = action_param 

		self.condStr = '"{}" {} "{}"'.format(self.cond_type, self.cond_operator, self.cond_param)
		self.condNum = '{} {} {}'.format(self.cond_type, self.cond_operator, self.cond_param)
		self.condition = None # This should be set to either condStr or condNum per subclass

	# methods for action types, 
	def disqualify(self):
		if not(eval(self.condition)):
			return
		elif(self.action_type == "Disqualify"):
			return True
		elif(self.action_type == "Qualify"):
			return False
		else:
			return "Not a valid action for this operand"

	def adjust(self):
		if not(eval(self.condition)):
			return
		elif(self.action_type == "Adjust"):
			return self.action_param
		else:
			return "Not a valid action for this operand"

# Helper classes, per condition operand

class StateOfResidence(Operand):
	def check(self):
		pass

	def exec(self):
		self.condition = self.condStr
		disqualify()

class NotStateOfResidence(Operand):
	def check(self):
		if(">=" in self.cond_operator):
			print("Operator Not Allowed")

	def exec(self):
		if not(eval(self.condStr)):
			return
		elif(eval(self.condStr) and self.action_type == "Disqualify"):
			return True
		elif(eval(self.condStr) and self.action_type == "Qualify"):
			return False
		else:
			return "Not a valid action for this operand"

class CreditScore(Operand):
	def check(self):
		pass

	highestTier = 0 
	def getHighest(self):
		if(self.cond_param > CreditScore.highestTier):
			print('{} is now the highest matching credit tier'.format(self.cond_param))
		else: return

	def exec(self):
		self.getHighest()
		if not(eval(self.condNum)):
			return
		elif(eval(self.condNum) and self.action_type == "Adjust"):
			return self.action_param
		else:
			return "Not a valid action for this operand"

class ProductName(Operand):
	def check(self):
		pass

	def exec(self):
		if not(eval(self.condStr)):
			return
		elif(eval(self.condStr) and self.action_type == "Adjust"):
			return self.action_param
		else:
			return "Not a valid action for this operand"

