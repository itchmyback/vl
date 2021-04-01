#! /usr/bin/env python3

import person
import product
import operand

class RulesEngine:
	def __init__(self, person, product, rules):
		self.person = person # class Person
		self.product = product # class Product
		self.rules = rules # data -- string or array?

	# main execution statement	
	def runRules(self):
		# Iterate through the rules list
		# Parse out each line
		# Instantiate an object depending on the type of condition operand
		# Helper objects will determine the results
		# The RulesEngine will handle any updates to top level instance inputs ie person, product, etc

# 		print(rules)	
		for line in rules:
			line = line.rstrip() # remove return characters
			lineArray = line.split(",") # split by comma delimiter
			print(lineArray)
		
		cond_type = None
		cond_operator = None
		cond_param = None
		action_type = None
		## action_operator assumed to be + for now
		action_param = None

		## (DEBUG) Create cond_type dictionary and get
		cond_type = "Florida"
		cond_operator = "=="
		cond_param = "Florida"
		action_type = "adjust"
		action_param = 0.7

		sor = operand.StateOfResidence(cond_type, cond_operator, cond_param, action_type, action_param)
#		sor.check()

		cond_type = 680 
		cond_operator = ">="
		cond_param = 700
		action_type = "Adjust"
		action_param = 0.7
	
		print('{} {} {} {} {}'.format(cond_type, cond_operator, cond_param, action_type, action_param))
		
		cs = operand.CreditScore(cond_type, cond_operator, cond_param, action_type, action_param)
		print(cs.exec())

		cond_type = "7-1 ARM" 
		cond_operator = "=="
		cond_param = "7-1 ARM" 
		action_type = "Adjust"
		action_param = 0.4

		print('{} {} {} {} {}'.format(cond_type, cond_operator, cond_param, action_type, action_param))

		pn = operand.ProductName(cond_type, cond_operator, cond_param, action_type, action_param)
		print(pn.exec())
		
# MAIN body
aperson = person.Person(720, "Florida")
aproduct = product.Product("7-1 ARM", 5.0, False)
rules = "0"

# Function to get rules by opening file and saving to list, line by line
def loadRules():
	file = open("rules_finance.csv", "r")
	arrayList = file.readlines()

	for line in arrayList:
		line = line.rstrip() # remove return characters
		line = line.split(",") # split by comma delimiter
#		print(line)

	file.close()
	return arrayList

# Call loadRules() to populate a rules list
rules = loadRules()
# print(rules)

# Instantiate RulesEngine
rules_engine = RulesEngine(aperson, aproduct, rules)

# Run the rules engine
rules_engine.runRules()
