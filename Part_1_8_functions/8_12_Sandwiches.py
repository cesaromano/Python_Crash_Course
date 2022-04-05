#Escribe una funcion que acepte una lista de items que una persona quiera en un
#sandwich. La funcion debe tener un parametro que colecte tantos items como
#el llamado de la funcion pueda proveer, y debera imprimir un resumen del
#sandwich que ha sido ordenado. LLama la funcion tres veces, usando un numero diferente
#de argumentos cada vez.

def hacer_sandwich(*items):
	"""Crea un sandwich"""
	print("\nSe ha armado un sandwich con los siguientes ingredientes:")
	for item in items:
		print(f"- {item}")

hacer_sandwich('pollo')
hacer_sandwich('pollo', 'puerco')
hacer_sandwich('pollo', 'puerco', 'pez')