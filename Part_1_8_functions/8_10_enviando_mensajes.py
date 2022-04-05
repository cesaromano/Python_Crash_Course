#Inicia con una copia del programa anterior, escribe una funcion llamada
#enviar_mensajes() que imprima cada mensaje y mueva cada mensaje a una nueva 
#lista llamada mensajes_enviados una vez que son impresos. Despues de llamar la
#funcion, imprime ambas listas para asegurarte que el mensaje fue movido
#correctamente.

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
mostrar_mensajes(mensajes[:], mensajes_enviados)

print(mensajes)
print(mensajes_enviados)


