#! /usr/bin/env python3

import person
import product
import rulesengine
		
# MAIN body

# Start
aperson = person.Person(720, "Florida")
aproduct = product.Product("7-1 ARM", 5.0, False)

print("\n###")
print('Person - state and credit score: {} and {}'.format(aperson.state, aperson.credit_score))
print('Product - name and starting interest rate: {} and {}'.format(aproduct.name, aproduct.interest_rate))
print("###\n")

# Call loadRules() to populate a rules list
rules = rulesengine.loadRules("rules_finance.csv")
# rules = rulesengine.loadRules("rules_finance_exception.csv")

# Instantiate RulesEngine
rules_engine = rulesengine.RulesEngine(aperson, aproduct, rules)

# Run the rules engine
rules_engine.runRules()
rules_engine.printOutput()

# Start
aperson = person.Person(500, "Texas")
aproduct = product.Product("30 YEAR FIXED", 4.0, False)

print("\n###")
print('Person - state and credit score: {} and {}'.format(aperson.state, aperson.credit_score))
print('Product - name and starting interest rate: {} and {}'.format(aproduct.name, aproduct.interest_rate))
print("###\n")

# Call loadRules() to populate a rules list
rules = rulesengine.loadRules("rules_finance.csv")
# rules = rulesengine.loadRules("rules_finance_exception.csv")

# Instantiate RulesEngine
rules_engine = rulesengine.RulesEngine(aperson, aproduct, rules)

# Run the rules engine
rules_engine.runRules()
rules_engine.printOutput()
