#! /usr/bin/env python3

import fibo

print("Hello World!")

# comment

## name = input("What is your name? ")
name = "John"
print("Hello " + name)

## birth_year = input("Enter your birthyear: ")
birth_year = "1978"
# age = 2020 - birth_year
# TypeError - int - str

age = 2020 - int(birth_year)
print(age)

# use Fibonacci functions imported from fibo
fibo.fib(1000)

# learning a class, not really setup properly here
class EmployeeA:
	pass

emp_a = EmployeeA()
emp_b = EmployeeA()

print(emp_a)
print(emp_b)

emp_a.first = "Corey"
emp_a.last = "Schafer"
emp_a.pay = 50000

emp_b.first = "Test"
emp_b.last = "User"
emp_b.pay = 60000

print(emp_a.pay)
print(emp_b.pay)

# a true class setup
class Employee0:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

# What happens if we leave self out of the method?
	def firstname():
		return '{}'.format(self.first)
# Gives a TypeError - 

emp_1 = Employee0("Corey", "Schafer", 50000)
emp_2 = Employee0("Test", "User", 60000)

print('{} {}'.format(emp_1.first, emp_1.last))

# Let's instead go back up and add a method to print full name
print(emp_1.fullname())
print(emp_2.fullname())

# print(emp_1.firstname())
# TypeError: firstname() takes 0 positional arguments but 1 was given

# The same as emp_1.fullname()
print(Employee0.fullname(emp_1))

# instantiate imported class
who = fibo.TheGuy("Fibonacci")
print(who.his_name)
