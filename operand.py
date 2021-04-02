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

	# Action type tests, to pick and choose into subclasses
	def ruleTest(self):
		if(eval(self.condition)):
			return True

	def disqualify(self):
		if(self.action_type == "Disqualify"):
			return True

	def adjust(self):
		if(self.action_type == "Adjust"):
			return float(self.action_param)

	# new action types
	def qualify(self):
		if(self.action_type == "Qualify"):
			return False

	def contact(self):
		if(self.action_type == "Contact"):
			return str(self.action_param)

# Subclasses per Condition Operand ie cond_type
class StateOfResidence(Operand):
	def check(self):
		pass

	def exec(self):
		self.condition = self.condStr
		if not(self.ruleTest()):
			return
		if(self.disqualify() != None):
			return self.disqualify()
		if(self.qualify() != None):
			return self.qualify()
		raise Exception("Not a valid action")

class CreditScore(Operand):
	def check(self):
		pass

	highestTier = 0 # This must change as instances update it
	finalCreditAdj = 0 # This is the final interest modified by all credit score rules

	# This is mostly a static method
	# This action type will have to processed in the RulesEngine
	def getHighest(self):
#		print('highestTier {}'.format(CreditScore.highestTier))
		# This must be gte, otherwise repeated execution calls will fail because cred_score is not > cred_score
		if(int(self.cond_param) >= CreditScore.highestTier):
			CreditScore.highestTier = int(self.cond_param)
			CreditScore.finalCreditAdj = float(self.action_param)
			print('{} is now the highest matching credit tier'.format(self.cond_param))
			print('{} is now the highest matching credit adjustment'.format(self.action_param))
			return True
		else: return False

	def exec(self):
		self.condition = self.condNum
		if not(self.ruleTest()):
			return
		if (self.getHighest() != None):
			return
# Can no longer adjust interest rate based on out of order execution of credit score rules
#		if not(self.getHighest()):
#			return
#		if(self.adjust != None):
#			return self.adjust()
		raise Exception("Not a valid action")

class ProductName(Operand):
	def check(self):
		pass

	def exec(self):
		self.condition = self.condStr
		if not(self.ruleTest()):
			return
		if(self.adjust != None):
			return self.adjust()
		if(self.contact != None):
			return self.contact()
		raise Exception("Not a valid action")
