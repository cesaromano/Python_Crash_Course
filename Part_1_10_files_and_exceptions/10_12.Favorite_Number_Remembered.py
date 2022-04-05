#Combine the two programs from Exercise 10-11 into one file. If the 
#number is already stored, report the favorite number to the user. If not
#prompt for the user's favorite number and store it in a file. Run 
#the program twice to see that it works.

import json

def get_number():
	"""Get favourite number of the user"""
	filename = input("What is the filename? ")

	try:

		with open(filename) as f:
			fav_number = json.load(f)

	except FileNotFoundError:

		fav_number = input("What is your favorite number? ")
		with open(filename, 'w') as f:
			json.dump(fav_number, f)
			print(f"We'll remember your number when you come back")

	else:

		print(f"I know your favorite number! It's {fav_number}")
	
get_number()