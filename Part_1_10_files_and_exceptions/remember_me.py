#*Saving and Reading User-Generated Data
#import json

#username = input("What is your name? ")

#filename = 'username.json'
#with open(filename, 'w') as f:
#	json.dump(username, f)
#	print(f"We'll remember you when you come back, {username}!")

#json.dump() and json.load() in same code

#import json

#Load the username, if it has been stored previously
#Otherwise, prompt for the username and store it
#filename = input('What is the filename?')
#try:
#	with open(filename) as f:
#		username = json.load(f)
#except FileNotFoundError:
#	username = input("What is your name? ")
#	with open(filename, 'w') as f:
#		json.dump(username, f)
#		print(f"We'll remember you when you come back, {username}")
#else:
#	print(f"Welcome back,{username}")

#*Refactoring

#import json

#def greet_user():
#	"""Greet the user by name."""
#	filename = input('What is the filename?')
#	try:
#		with open(filename) as f:
#			username = json.load(f)
#	except FileNotFoundError:
#		username = input("What is your name? ")
#		with open(filename, 'w') as f:
#			json.dump(username, f)
#			print(f"We'll remember you when you come back, {username}")
#	else:
#		print(f"Welcome back,{username}!")

#greet_user()

#import json

#def get_stored_username():
#	"""Get stored username if available."""
#	filename = input('What is the filename?')
#	try:
#		with open(filename) as f:
#			username = json.load(f)
#	except FileNotFoundError:
#		return None
#	else:
#		return username

#def greet_user():
#	"""Greet the user by name."""
#	username = get_stored_username()
#	if username:
#		print(f"Welcome back,{username}!")		
#	else:
#		filename = input('What is the filename?')
#		username = input("What is your name? ")
#		with open(filename, 'w') as f:
#			json.dump(username, f)
#			print(f"We'll remember you when you come back, {username}")
		

#greet_user()

import json

def get_stored_username():
	"""Get stored username if available."""
	filename = input('What is the filename?')
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else: 
		values = {'filename' : filename, 'username' : username}
		return values

def get_new_username():
	"""Prompt for a new username."""
	value = get_stored_username()
	filename = value_1['filename']
	username = input("What is your name? ")
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greet_user():
	"""Greet the user by name."""
	value = get_stored_username()
	username = value['username']
	if username:
		print(f"Welcome back,{username}!")		
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}")
		

greet_user()