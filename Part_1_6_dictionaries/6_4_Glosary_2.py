#Toma el ejemplo 6_3, reemplaza las series de print() por un loop que corra 
#a lo largo de las llaves y valores del diccionario.

glosario = {
	'identar' : 'Correr cuatro espacios hacia la derecha.',
	'loop' : 'Funcion para repetir un fragmeto de codigo de programacion.',
	'if' : 'Declaracion que se usa para realizar una accion dependiendo de un estado, informacion de tipo booleano.',
	'variable' : 'Informacion asociada a un nombre.',
	'string' : 'Tipo de informacion que se caracteriz por estar entre comillas.',
	'Diccionario' : 'Declaracion para almacenar pares de claves-valores.',
	'clave' : 'Nombre de un valor asociado en un diccionario.',
	'valor' : 'Pedazo de informacion asociado a una clave en un diccionario.',
	'lista' : 'Serie de valores separados por comas.',
	'editor de texto' : 'Programa que traduce y organiza los comandos de python.',
}

for clave, valor in glosario.items():
	print(f"{clave.title()}:")
	print(f"\t\t{valor}\n.")