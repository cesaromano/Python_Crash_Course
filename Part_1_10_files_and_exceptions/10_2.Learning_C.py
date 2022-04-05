#	Learning_C

#file = 'biblia.txt'

with open('biblia.txt') as file_object:
	for line in file_object:
		message = line.replace('Biblia', 'panocha')
		print(message)
