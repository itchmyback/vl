#! /usr/bin/env python3

import person
import product
import rules_engine
		
# MAIN body
aperson = person.Person(720, "Florida")
aproduct = product.Product("7-1 ARM", 5.0, False)

# Call loadRules() to populate a rules list
rules = rules_engine.loadRules()

# Instantiate RulesEngine
rules_engine = rules_engine.RulesEngine(aperson, aproduct, rules)

# Run the rules engine
rules_engine.runRules()
