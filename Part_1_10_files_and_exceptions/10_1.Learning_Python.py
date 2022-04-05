#Learning Python

filename = 'Documentacion de actividades.txt'

with open(filename) as file_object:

#Letura total del contenido
#	content = file_object.read()

#print(content.rstrip())

#Lectura linea por linea

#	for line in file_object:
#		print(line.rstrip())

#Lectura desde una lista

	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())