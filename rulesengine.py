#! /usr/bin/env python3

import person
import product
import operand

class RulesEngine:
	def __init__(self, person, product, rules):
		self.person = person # class Person
		self.product = product # class Product
		self.rules = rules # data -- string or array?
		
		# reset static class variable for Operand(CreditScore.highestTier))
		operand.CreditScore.highestTier = 0
		operand.CreditScore.finalCreditAdj = 0
		
		# static variable for new action alert
		alertMsg = None

	# main execution statement	
	def runRules(self):
		# Iterate through the rules array input
		# Instantiate an object depending on the type of condition type - state_of_residence, credit_score, product_name
		# Helper objects will determine the results
		# The RulesEngine will handle any updates to top level instance inputs ie person, product, etc
		## In fact, the RulesEngine should probably handle all the outputs
		
#		cs = [None] * len(self.rules) # This seems overly complicated to initialize
#		print(cs)

		# Iterate through the rules list, use an index 'i' so that rule objects can be created with that index
		for i, part in enumerate(self.rules):
			# function scope variables				
			cond_type = part[0]
			cond_operator = part[1]
			cond_param = part[2]
			action_type = part[3]
			## action_operator assumed to only be + for now
			action_param = part[4]
			print('{} {} {} {} {}'.format(cond_type, cond_operator, cond_param, action_type, action_param))

			# Instantiate an object
			# Create by index so that each instance is unique, otherwise class level variables will be lost such as highest credit tier
				# Also, don't append, insert as the indexes are disjointed between the condition types
			# Pass in top level instance inputs such as person and product vars	
			# Use If-Then logic on cond_type, but can extend to switch case for additional conditioon operands
			# By using helper classes, there is an extra step to fetch pass/fail condition of each rule			
			
			if(cond_type == "state_of_residence"):
				sor = operand.StateOfResidence(self.person.state, cond_operator, cond_param, action_type, action_param)
#				print('sor execution is {}'.format(sor.exec()))
				if not (sor.exec() == None):
					self.product.disqualified = sor.exec()	
					print(self.product.disqualified)
			elif(cond_type == "credit_score"):
				cs = operand.CreditScore(self.person.credit_score, cond_operator, cond_param, action_type, action_param)
#				cs.insert(i, operand.CreditScore(self.person.credit_score, cond_operator, cond_param, action_type, action_param))
#				print('cs execution is {}'.format(cs[i].exec()))
				if(cs.exec()): 
#				if(cs[i].exec()): 
					# This calculation will be handled using a final static approach
#					self.product.interest_rate = self.product.interest_rate + cs[i].exec()
					print(self.product.interest_rate)
			elif(cond_type == "product_name"):
				pn = operand.ProductName(self.product.name, cond_operator, cond_param, action_type, action_param)
#				print('pn execution is {}'.format(pn.exec()))
				if(pn.exec()):
					self.product.interest_rate = self.product.interest_rate + pn.exec()
					print(self.product.interest_rate)
			else:
				pass # Assume header

		# Static Credit Score determination
#		print(operand.CreditScore.finalCreditAdj)
		self.product.interest_rate = self.product.interest_rate + operand.CreditScore.finalCreditAdj
			

	# Final Outputs
	def printOutput(self):
		print("\n###")
		print("Is the product disqualified?", self.product.disqualified)
		print("Final interest rate: ", self.product.interest_rate)
#		print("Actions to take: ", pn.action_param)
		print("###\n")

# Function to get rules by opening file and saving to list, line by line, and then process to a string array
def loadRules(path):
	file = open(path, "r")
	lineList = file.readlines()
	arrayList = [] # outputList

	for line in lineList:
		line = line.rstrip() # remove return characters
		line = line.split(",") # split by comma delimiter
		arrayList.append(line)

	file.close()
	return arrayList
