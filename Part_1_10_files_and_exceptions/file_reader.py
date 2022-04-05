# 10. FILES AND EXEPTIONS
#Work with files to analyze lots of data
#exeptions, especial objects Python creates to manage errors
#that arise while a program is running
#json module, alowws to save user data so it isn't lost when program
#stops running

#	Reading from a file
#Reading from a file is particulary useful in data analysis applications
#but it's also applicable to any situation in which you want to analyze
#or modify information stored in a file.

#*Reading an entire file

#with open('pi_digits.txt') as file_object:
#	contents = file_object.read()
#print(contents.rstrip())

#*File paths
#to get pyhton to open files from a directory other than the one where
#your program file is stored , you need to provide a file path, wich
#tells python to look in a specific location on your system.

#with open('text_files/pi_digits.txt') as file_object:
#	contents = file_object.read()
#print(contents.rstrip())

#to open a file regaardless of where the program thats beign executed
#is stored use absolute file path. it can be used when relative path
#doesn't work
#you'll need to write out a full path to clarify where you want Python
#to look.

#file_path = 'C:/Users/guazo/OneDrive/Documentos/TRABAJOS/impagricus/Resumen del proyecto/pi_digits.txt'
#with open(file_path) as file_object:
#	contents = file_object.read()
#print(contents.rstrip())

#*Reading line by line
#you cann use a for loop on the file object to examine each line from
#a file 

#filename = 'pi_digits.txt'

#with open(filename) as file_object:
#	for line in file_object:
#		print(line.rstrip())

#*Making a list of lines from a file
#If you want to retain access to a file's contents outside the with block
#you can store the file's lines in a list inside the block and then
#work with that list

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())