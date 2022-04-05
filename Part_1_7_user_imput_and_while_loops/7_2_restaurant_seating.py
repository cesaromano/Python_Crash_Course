#Escribe un programa que le pregunte al usuario cuantas personas hay en el grupo
#para cenar, si la repuesta es mas de 8, imprime un mensaje diciendo que deben
#esperar por una mesa. De lo contrario, reporta que la mesa esta lista.

personas = input("Cuantos van a cenar esta noche? ")
personas = int(personas)

if personas >= 8:
	print("En ese caso deberan esperar un poco")
else:
	print("Su mesa esta lista")