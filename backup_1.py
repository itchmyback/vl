#! /usr/bin/env python3

import person
import product

class RulesEngine:
	def __init__(self, person, product, rules):
		self.person = person # class Person
		self.product = product # class Product
		self.rules = rules # data, string or array?

## Redo to include a formal rules engine setup, use double hash comments


	def loadRules():
		## UPDATE - ignore below statements, the approach upon further examination is looking for a business rules or drools type of implementation
		## Open file, read contents into a List, close file, return the list
			
		## 11. Open CSV file for reading and parse line by line (each rule will be on a line, no salience, processed in order)

		file = open("rules_finance.csv", "r")
		lineList = file.readlines()
		file.close()

#		print(lineList[1])
		return lineList

	def runRules(self):
		## UPDATE - the logic here will probably have to be transferred to a rules based setup			
		## What now? switch? Make an object maybe - maybe make an object based on switch
		## The issue is do we need that many objects created? It's really just a bunch of if/then statements
		## Maybe construct the string and run eval? A condition B, then C op D
		## Doing that is simplest, so an assumption will have to be made that code exists to limit the user input
		## ie something to now allow comparison of state as gte
	## Rules Engine 
		## 12. Fetch condition type: state_of_residence, credit_score, product_name
		## 13. Fetch condition operator: gte, lt, equal, not_equal - or should users just be trained in actual symbols?
		## 14. Fetch condition parameter
		## 15. Fetch action type
		## 16. Fetch action parameter

		cond_type = None
		cond_operator = None
		cond_param = None
		action_type = None
		## action_operator assumed to be + for now
		action_param = None

		## Create cond_type dictionary and get
		cond_type = "Florida"
		cond_operator = "=="
		cond_param = "Florida"

		def getState():
			return self.person.state

		def getCredScore():
			return self.person.credit_score

		def getProdName():
			return self.product.name

		def cond_type_switch(cond_type):
			switcher = {
				"state_of_residence": getState,
				"credit_score": getCredScore,
				"product_name": getProdName
			}
			switchfunc = switcher.get(cond_type, lambda: "Invalid Condition")
			return switchfunc()

		print(cond_type_switch("state_of_residence")) # DEBUG
			
		## Concatenate string and evaluate
		## Must add quotes to transform string arguments back to string type
		## This makes the eval method less global as it would require processing between string and number
		## Assume condition operator is input in Python format
		rule_eval_statement = '"{}" {} "{}"'.format(cond_type_switch("state_of_residence"), cond_operator, cond_param)
		print(rule_eval_statement)

		print(eval(rule_eval_statement))

		print(self.rules) # DEBUG
		# Assume standard set of rules -
		# 1. check if the product is offered in a particular state
		# 2. if so, run the appropriate calculations 
		# 3. range of credit scores will be considered a constant range from 300 to 850
		# 4. credit score matching to tier will be assumed to target highest possible tier

		# Check for disqualified states
		# State and product are declared, but perhaps normally a list of qualifying states would have to be fetched per product or vice-versa
#		print(self.person.state)
		if(self.person.state) in self.rules[1]:
			self.product.disqualified = True
		else:
			self.product.disqualified = False

		if(self.product.disqualified == False):
			print(self.product.name + " not offered in " + self.person.state)
			return
		else: # Else product is offered and interest rate can be calculated

			# credit score 
			# There are probably credit score ranges, so what would the data look like?
			# Maybe a table, with tier cutoffs, processed high to low
			# start | modifier (this string needs to be fetched and applied to the calculation, in theory could be any math op)
			# 720  | + 0.5 
			# 300  | - 0.3
			# From online suggestions, will attempt to use eval() safely for the case of any math operation
			# However, maybe for now we will assume adjustments are strictly additive
			if(self.person.credit_score >= self.rules[2]):
#				Any math defined explicitly in the method will work
				return self.product.interest_rate + self.rules[3]
#				return self.product.interest_rate eval(self.rules[3])
				
			else:
				return self.product.interest_rate
		
# MAIN body
aperson = person.Person(720, "Florida")
aproduct = product.Product("7-1 ARM", 5.0, False)

# print(aperson)
# print(aproduct)

# print(aperson.credit_score)

# get rules
testrules = RulesEngine.loadRules()
print(testrules)

stateList = ["Texas", "New York", "California", "Florida"]
# print(stateList.index("Florida"))
# index() would require try exception handling

#if "Florida" in stateList:
#	print("true")
#else:
#	print("false")

rules = ["Hello World", stateList, 720, 0.05]

# rules would probably have a list of states the product is offered in 
# and interest rate modifier by score tier

def zero():
	return "zebo"

def one():
	return aperson.state

# practice switch statement
def a_switch(arg):
	switcher = {
#		"0": aperson.state, # string object not callable
		1: "number"
	}

	return switcher.get(arg, "Invalid")
# print(a_switch("0"))

def  numbers_to_strings(arg):
	switcher = {
		0: zero,
		"b": one,
#		2: aperson.state # string object not callable
#		2: "two" # this is also not callable?
		2: zero
	}
#	return switcher.get(arg, "Invalid")
	func = switcher.get(arg, lambda: "Invalid")
	return func()
# print(numbers_to_strings(2))




# Instantiate RulesEngine
rules_engine = RulesEngine(aperson, aproduct, rules)

print(rules_engine.runRules())
