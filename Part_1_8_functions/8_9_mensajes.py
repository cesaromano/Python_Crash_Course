#Realiza una lista que contenga series de mensajes cortos. Pasa lalista a una
#funcion llamada mostrar_mensajes(), la cual imprima cada mensaje

def mostrar_mensajes(mensajes):
	"""Imprime mensajes cortos tomados de una lista"""
	for mensaje in mensajes:
		print(mensaje)

mensajes = ['concha', 'pito', 'tetas', 'hoyo']
mostrar_mensajes(mensajes)
