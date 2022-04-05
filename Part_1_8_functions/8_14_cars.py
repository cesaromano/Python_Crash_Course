#Escribe una funcion que almacene informacion acerca de un carro en un diccionario
#la funcion debera recibir siempre un manufacturero y un nombre de modelo. Debera
#aceptar tambien un numero arbitrario de argumentos keyword. Llama la funcion con
#la informacion requerida y otros dos pares clave-valor, tales como color o una
#caracteristica opcional. Imprime el dicccionario retornado para asegurarte que
#toda la informacion ha sido almacenada correctamente.

def construccion_carro(manufactura, modelo, **informacion_carro):
	"""Construye un diccionario con los parametros del carro"""
	informacion_carro['manufactura'] = manufactura
	informacion_carro['modelo'] = modelo
	return informacion_carro

carro = construccion_carro('renault', 'sandero', color= 'gris', hashback= True)
print(carro)
