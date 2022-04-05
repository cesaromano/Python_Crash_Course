#Has un diccionario llamado ciudades, usa el nombre de tres ciudades como llaves
#

ciudades = {
	'bogotá': {
		'pais' : 'Colombia',
		'poblacion' : '7 millones',
		'datos importantes' : 'Es la capial de colombia',
	},
	'rio de janeiro': {
		'pais' : 'Brasil',
		'poblacion' : '6 millones',
		'datos importantes' : 'El cristo redentor es una de las 9 maravillas'
		'del mundo',
	},
	'bucaramanga': {
		'pais' : 'Colombia',
		'poblacion' : '581 mil',
		'datos importantes' : 'Se le conoce como laciudad bonita',
	},

}

#for ciudad, descripciones in ciudades.items():
#	print(f"\n{ciudad.title()}")
#	pais = descripciones['pais']
#	poblacion = descripciones['poblacion']
#	dato_importante = descripciones['datos importantes']

#	print(f"\tPais: {pais.title()}")
#	print(f"\tPoblacion: {poblacion.title()}")
#	print(f"\tDato importante: {dato_importante.title()}")

for ciudad, descripciones in ciudades.items():
	print(f"\n{ciudad.title()}")
	print(f"\t{descripciones}")