#Wrap your code from Exercise 10-6 in a while loop ao the user can
#continue entering numbers even if they make a mistake and enter text
#instead of a number.

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