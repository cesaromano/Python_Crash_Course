#One common problem when prompting for numerical input occurs when people
#provide text instead of numbers. When you try to convert the input to 
#an int, you'll get a ValueError. Write a program that prompts for
#two numbers. Add them togeether and print the result. Ctch the ValueError
#if either input is not a number, and print a friendly error message.
#Test your program by entering two numbers and then by entering some
#text instead of a number

def add_numbers(num_1, num_2):
	"""Add two numbers given by user"""

	try: 

		num_1 = int(num_1)
		num_2 = int(num_2)

	except ValueError:

		print("You can only give numbers to add")

	else:

		addition = num_1 + num_2
		print(f"The result of addition is: {addition}")




num_1 = ""

while True:

	num_1 = input("Write first number to add or 'q' to quit: ")
	if num_1 == "q":
		break
	num_2 = input("Write second number to add or 'q' to quit: ")
	if num_2 == "q":
		break
	
	add_numbers(num_1, num_2)