#Inicia con el codigo del programa anterior. llama la funcion enviar_mensajes()
#con una copia de la lista de mensajes. Despues de llamarla funcion imprime
#ambas listas para mostrar que la lista original retuvo los mensajes

def mostrar_mensajes(mensajes, mensajes_enviados):
	"""Imprime mensajes cortos tomados de una lista"""
	mensajes.reverse()
	while mensajes:
		mensaje_actual = mensajes.pop()
		print(mensaje_actual)
		mensajes_enviados.append(mensaje_actual)

mensajes = ['hola como estas', 'que te importa', 'come torta', 'que tu mama es' 
'una gorda']
mensajes_enviados = []
mostrar_mensajes(mensajes, mensajes_enviados)

print(mensajes)
print(mensajes_enviados)