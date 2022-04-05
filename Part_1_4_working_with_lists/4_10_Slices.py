#usando un ejemplo anterior, imprime los siguientes mensajes:
#una lista de los tres primeros items 
multiplos = [valor*3 for valor in range (1, 31)]
print(multiplos)
print(f"Los tres primeros multiplos de tres son: {multiplos [:3]}")
#tres items de la mitad de la lista
print(f"Los tres multiplos del medio de la lista son: {multiplos[13:16]}")
#los ultimos 3 items de la lista
print(f"Los ultimos tres multiplos de la lista son: {multiplos[-3:]}")