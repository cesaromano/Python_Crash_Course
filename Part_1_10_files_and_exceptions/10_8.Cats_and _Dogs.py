#Make two files, cats.txt and dogs.txt. Store at least three names of
#cats in the first file and three names of dogs in the second file. Write
#a program that tries to read these files and print the contents of the
#file to the screen. Wrap your code in a try-except block to catch the
#FileNotFound Error, and print a friendly message if a file is missing.

filename_1 = "cats.txt"
filename_2 = "dogs.txt"

try:

	with open(filename_1) as f_1:
		content_1 = f_1.read()
		print(content_1)

	with open(filename_2) as f_2:
		content_2 = f_2.read()
		print(content_2)

except FileNotFoundError:
	print("The file is missing")