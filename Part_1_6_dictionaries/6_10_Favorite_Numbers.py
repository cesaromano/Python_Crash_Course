#Modifica el programa del ejercicio 6_2 de manera que cada persona tenga mas de 
#un numero favorito:

numeros_favoritos = {
	'romano' : [9, 6, 3, 14],
	'sergio' : [14, 16, 1, 33],
	'rosalba' : [23, 32, 16, 8],
	'victor' : [17,5, 6, 100],
	'marta' : [2, 3, 4, 5],
}

#Imprime el nombre de cada persona junto con sus numeros favoritos 

for nombre, numeros in numeros_favoritos.items():
	print(f"\nLos numeros favoritos de {nombre.title()} son:")
	for numero in numeros:
		print(f"\t{numero}")