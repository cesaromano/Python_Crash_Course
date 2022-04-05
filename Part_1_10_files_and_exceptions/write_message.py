#	WRITING TO A FILE
#* Writing to an empty file

#filename = 'programing.txt'

#with open(filename, 'w') as file_object:
#	file_object.write("I love programming.")

#* Writing Multiple Lines

#filename = 'programing.txt'

#with open(filename, 'w') as file_object:
#	file_object.write("I love programming.\n")
#	file_object.write("I love creating new games.\n")

#* Appending to a file

filename = 'programing.txt'

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating aps that can run in a browser.\n")