#Escribe una funcion llamada hacer_camiseta() que acepte un tamaño y el texto
#de un mensaje que debera ser impreso en la camiseta. La impresion deberia
#imprimir una oracion resumiendo la talla de la camiseta y el mensaje impreso
#en ella, llama la funcion utilizando argumentos posicionales, llama la funcion
#una segunda vez usando keyword arguments.

def hacer_camiseta(talla, mensaje):
	print(f'La talla de la camiseta es {talla} y su mensaje es "{mensaje}"')

hacer_camiseta(14, 'acariciadores de pelotas')
hacer_camiseta(talla= 14, mensaje= 'acariciadores de pelotas')
hacer_camiseta(mensaje= 'acariciadores de pelotas', talla= 14)