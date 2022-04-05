#Realiz un diccionario que contenga los tres rios mas grandes y el pais de cada
#rio:

rios = {
	'amazonas' : 'colombia, brasil y peru',
	'nilo' : 'egipto',
	'yangtse' : 'china',
}

#Usa un loop para imprimir una oracion acerca de cada rio:

#for rio, pais in rios.items():
#	print(f"El rio {rio.title()} es el puto rio de {pais.title()}.")

#Usa un loop para imprimir el nombre de cada rio en el diccionario:

#for rio in rios.keys():
#	print(rio.title())

#Usa un loop para imprimir el nombre de cada pais en el diccionario:

for pais in rios.values():
	print(pais.title())