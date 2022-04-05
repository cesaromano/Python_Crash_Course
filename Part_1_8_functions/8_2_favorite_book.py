#Escribe una funcion llamada libro_favorito() que acepte un parametro "titulo".
#La funcion deberia imprimir un mensaje, llama la funcion y asegurate que el 
#titulo del libro este incluido como un argumento en la funcion llamada.

def libro_favorito(titulo):
	"""Muestra mensaje con nombre del titulo"""
	print(f"Mi puto libro favorito es {titulo.title()}")

libro_favorito('el emilio')