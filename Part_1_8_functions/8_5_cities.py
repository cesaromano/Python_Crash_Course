#Escribe una funcion llamada descripcion_ciudad() que acepte el nombre de una
#ciudad y su pais, la funcion debe imprimir una simple oracion, entrega el 
#parametro del pais como valor por defecto. LLamaa tu funcion para tres ciudades
#diferentes, con almenos una que no este en pais por defecto

def descripcion_ciudad(ciudad, pais= 'colombia'):
	print(f"La ciudad de {ciudad.title()} queda en {pais.title()}")

descripcion_ciudad('bogota')
descripcion_ciudad('villavicencio')
descripcion_ciudad('rio de janeiro', pais= 'brasil')