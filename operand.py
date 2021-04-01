#! /usr/bin/env python3

# Helper classes - super and sub, for returning values from rules when they fire or resolve to true
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

	# methods for action types  - disqualify, adjust
	def disqualify(self):
		if not(eval(self.condition)):
			return
		elif(self.action_type == "Disqualify"):
			return True
		elif(self.action_type == "Qualify"):
			return False
		else:
			return "Not a valid action for this condition type"

	def adjust(self):
		if not(eval(self.condition)):
			return
		elif(self.action_type == "Adjust"):
			return self.action_param
		else:
			return "Not a valid action for this condition type"

# Subclasses per Condition Operand ie cond_type

class StateOfResidence(Operand):
	def check(self):
		pass

	def exec(self):
		self.condition = self.condStr
		self.disqualify()

class CreditScore(Operand):
	def check(self):
		pass

	highestTier = 0 # This must change as instances update it

	def getHighest(self):
		print('highestTier {}'.format(CreditScore.highestTier))
		if(int(self.cond_param) > CreditScore.highestTier):
			CreditScore.highestTier = int(self.cond_param)
#			print('highestTier {}'.format(CreditScore.highestTier))
#			print('{} is now the highest matching credit tier'.format(self.cond_param))
		else: return

	def exec(self):
		self.getHighest()
		self.condition = self.condNum
		self.adjust()

class ProductName(Operand):
	def check(self):
		pass

	def exec(self):
		self.condition = self.condStr
		self.adjust()
