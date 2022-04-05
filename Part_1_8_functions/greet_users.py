#	PASANDO UNA LISTA
#Amenudo encontraras  util pasar una lista a una funcion. Cuando pasas
#una lista a una funcion, la funcion obtiene acceso directo a los contenidos de
#la lista. Usemos funciones para trabajar con listas mas eficientemente.

def saludo_usuarios(nombres):
	"""Imprime un simple saludo a cada usuario en la lista"""
	for nombre in nombres:
		msg = f"Hola, {nombre.title()}"
		print(msg)

usuarios = ['laura', 'angelica', 'carolina']
saludo_usuarios(usuarios)