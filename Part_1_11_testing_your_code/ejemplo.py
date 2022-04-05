#escribir en  un programa en el lenguaje de programación Python 
#que utilice variables y operadores el siguiente mensaje: 
#"Hola Misión TIC 2022... soy <nombre del estudiante>"

while True:
	name = input("Escribe tu nombre ó 's' para salir: ")
	if name == 's':
		break
	else: 
		print(f"Hola Misión TIC 2022... soy {name}")