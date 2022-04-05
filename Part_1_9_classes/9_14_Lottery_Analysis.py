from random import choice
#1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'e', 'i', 
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'e', 'i', 'o', 'u']
lista_2 = []
ticket = [8, 'i', 6, 2, 7]

numero = 1
conteo = 1

while lista_2 != ticket:
#	lista_2 = [0]
	conteo += 1
	print(lista_2)
	lista_2 = []
	numero = 1
	while numero <= 5 :
		elemento = choice(lista)
		print(elemento)
		
#	lista_2 = elemento.pop()
#		lista_2[0:3] = elemento
		lista_2.append(elemento)
		numero += 1
		
#	print(elemento)

print (f"El loop tuvo que correr {conteo} veces" 
	" para encontrar el codigo del ticket")

