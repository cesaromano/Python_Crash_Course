#	HACIENDO LISTAS NUMERICAS
#hay muchas razones para almacenar conjuntos de numeroscomo:
#- seguir la posicion de cada caracter en un juego 
#- seguir la posicion de los jugadores con puntajes mas altos
#- visualizacion de datos por medio de conjuntos de datos 
#Python provee una variedad de herramientas para para trabajar
#eficientemente con numeros

#*Usando la funcion range()
#la funcion range() genera series de numeros 
#for value in range(1, 5):
#	print(value)
#a pesar de que el ultimo valor es cinco, el programa solo imprime
#hasta el 4, esto es por el comportamiento uno a uno que a menudo se ve en
#los lenguajes de programacion. la funcion indica que se comience 
#con el primer valor que se entrega y se termine una vez que alcance el 
#segundo valor 
#para imprimir los numeros del 1 al 5 se debe usar el rango (1, 6)
#for value in range(1, 6):
#	print(value)
#for value in range(0, 6):
#	print(value)

#Usando range() para ahcer una lista de numeros
#se pueden usar los resultados de la funcion range() para crear una lista
#con la funcion list() 
#numbers = list(range(0, 6))
#print(numbers)

