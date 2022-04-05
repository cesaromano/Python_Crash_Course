from random import choice
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'e', 'i', 'o', 'u']
lista_2 = []

numero = 1

while numero <= 4:
	elemento = choice(lista)
#	lista_2 = elemento.pop()
	lista_2.append(elemento)
	numero += 1
#	print(elemento)

print (f"El ticket con el codigo {lista_2} gana un premio")

