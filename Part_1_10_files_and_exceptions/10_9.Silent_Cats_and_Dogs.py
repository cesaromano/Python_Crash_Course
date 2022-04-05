#Modify your except block in Exercise 10-8 to fail silently if either
#file is missing

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
	pass