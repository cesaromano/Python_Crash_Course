#Write a program that prompts for the user's favourite number.
#Use json.dumpt() to store this number in a file. Write a separate program
#that reads in this value and prints the message, "Iknow your favorite
#number! It's ____."

import json

def get_number():
	"""Get favourite number of the user"""
	fav_number = input("What is your favourite number? ")

	filename = 'favourite_number.json'
	with open(filename, 'w') as f:
		json.dump(fav_number, f)

get_number()