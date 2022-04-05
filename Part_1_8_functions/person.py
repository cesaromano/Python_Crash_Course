#*Retornando un diccionario
#Una funcion puede retornar cualquier tipo de valor que necesites, incluyendo
#estructuras de informacion mas complicadas como listas y dccionarios.

#def construir_persona(nombre, apellido):
#	"""Retornando un dicionario de informacion acerca de una persona."""
#	persona = {'nombre': nombre, 'apellido': apellido}
#	return persona

#musico = construir_persona('victor', 'garcia')
#print(musico)

#la funcion toma el nombre y el apellido y situa esos valores en un diccionario
#Los strings 'victor' y 'garcia' estan ahora etiquetados como nombre y apellido.
#Puedes extender esta funcion para aceptar valores opcionales como segundo
#nombre, edad, y ocupacion, o cualquier otra informacion que quieras almacenar
#de una persona.

def construir_persona(nombre, apellido, edad= None):
	"""Retornar un diccionario de informacion acerca de una persona."""
	persona = {'nombre': nombre, 'apellido': apellido}
	if edad:
		persona['edad'] = edad
	return persona

musico = construir_persona('victor', 'garcia', edad= 39)
print(musico)

#El valor especial None, se usa cuando una variable no tiene un valor especifico
#asignado. Piensa en este valor como un parametro de sustitucion. En test
#condicionales None evalua como Falso. 