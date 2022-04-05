#escribe una funcion llamada city_country() que tome en el nombre de una ciudad 
#y su pais. La funcion debria retornar un string con formato como este Santiago,
#Chile

def ciudad_pais(ciudad, pais):
	ciudad_mas_pais = f"\n{ciudad}, {pais}"
	return ciudad_mas_pais.title()
	print()

pais = ciudad_pais('bogota', 'colombia')
print(pais)

pais = ciudad_pais('rio de janeiro', 'brasil')
print(pais)

pais = ciudad_pais('villavicencio', 'colombia')
print(pais)