#EXCEPTIONS
#*Handling the ZeroDivisionError Exception
#try:
#	print(5/0)
#except ZeroDivisionError:
#	print("You can't divide by zero!")

#*Using Exceptions to Prevent Crashes

#print("Give me two numbers, and I'll divide them.")
#print("Enter 'q' to quit.")

#while True:
#	first_numer = input("\nFisrt number: ")
#	if first_numer == 'q':
#		break
#	second_numer = input("\nsSecond number: ")
#	if second_numer == 'q':
#		break
#	answer = int(first_numer) / int(second_numer)
#	print(answer)

#*The else Block

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_numer = input("\nFisrt number: ")
	if first_numer == 'q':
		break
	second_numer = input("\nsSecond number: ")
	if second_numer == 'q':
		break
	try:
		answer = int(first_numer) / int(second_numer)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)