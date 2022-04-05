#*Working with a file's content

#filename = 'pi_digits.txt'

#with open(filename) as file_object:
#	lines = file_object.readlines()

#pi_string = ''
#for line in lines:
#	pi_string += line.rstrip()
#or
#	pi_string += line.strip()


#print(pi_string)
#print(len(pi_string)) 

#*Large files:one million digits

#filename = 'pi_million_digits.txt'

#with open(filename) as file_object:
#	lines = file_object.readlines()

#pi_string = ''
#for line in lines:
#	pi_string += line.rstrip()
#or
#	pi_string += line.strip()


#print(f"{pi_string[:52]}...")
#print(len(pi_string))

#*Is your birthday contained in pi?

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
#	pi_string += line.rstrip()
#or
	pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
	print("Your birthday appears in the firs million digits of pi!")
else:
	print("Your birthday does not appears in the firs million digits of pi!")