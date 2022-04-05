#*Usando una funcion con un loop while
#Puedes usar funciones con todas las estructuras Python que has aprendido hasta 
#el momento.

def dar_formato_nombre(nombre, apellido):
	"""Retornar nombre completo con formato claro"""
	nombre_completo = f"{nombre} {apellido}"
	return nombre_completo.title()

#Este es un loop infinito
#while True:
#	print("\nPor favor dime tu nombre")
#	p_nombre = input("Nombre: ")
#	p_apellido = input("Apellido: ")

#	nombre_formato = dar_formato_nombre(p_nombre, p_apellido)
#	print(f"\nHola {nombre_formato}")

#Este loop no ofrece una salida al usuario
while True:
	print("\nPor favor dime tu nombre")
	print("(ingresa 'q' si quieres salir)")

	p_nombre = input("Nombre: ")
	if p_nombre == 'q':
		break
	p_apellido = input("Apellido: ")
	if p_apellido == 'q':
		break

	nombre_formato = dar_formato_nombre(p_nombre, p_apellido)
	print(f"\nHola {nombre_formato}")
