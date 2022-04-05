# Write a program that propmts the user for their name. When they respond
#write their name to a file called guest.txt

prompt = "Write your name: "

name = input(prompt)

filename = "guest.txt"

with open(filename, 'w') as file_object:
	file_object.write(name)