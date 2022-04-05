#Write a program that prompts for the user's favourite number.
#Use json.dumpt() to store this number in a file. Write a separate program
#that reads in this value and prints the message, "Iknow your favorite
#number! It's ____."

import json

def read_number():
	filename = 'favourite_number.json'
	with open(filename) as f:
		fav_number = json.load(f)
		print(f"I know your favorite number! It's {fav_number}")

read_number()