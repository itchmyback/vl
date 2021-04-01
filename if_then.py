#! /usr/bin/env Python
if(True):
	print(True)

if(True): print(True)

if True:
	print(True)

if True: print(True)

def prTr():
	if True: return "true"

print(prTr())

# if !True:  # incorrect syntax
if not(True):
	pass
else:
	print(False)

if not True:
	pass
else:
	print(False)
