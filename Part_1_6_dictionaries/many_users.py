#*Un diccionario en un diccionario
#Puedes anidar un diccionario dentro de otro diccionario pero tu codigo puede
#complicarse rapidamente. 
#En el siguiente listado, almacenaremos tres piezas de informacion acerca de 
#cada usuario: nombre, apellido y ubicacion. Accederemos a esta informacion 
#haciendo loop a lo largo de los nombres de usuarios y el diccionario de 
#informacion con cada nombre de usuario:

usuarios = {
	'aeinstein': {
	   'nombre': 'albert',
	   'apellido': 'einstein',
	   'ubicacion': 'princeton',
	},

	'mcurie': {
		'nombre': 'marie',
		'apellido': 'curie',
		'ubicacion': 'paris',
	},
}

for nombre_usuario, info_usuario in usuarios.items():
	print(f"\nUsuario: {nombre_usuario.title()}")
	nombre_completo = f"{info_usuario['nombre']} {info_usuario['apellido']}"
	ubicacion = info_usuario['ubicacion']

	print(f"\tNombre completo: {nombre_completo.title()}")
	print(f"\tUbicacion: {ubicacion.title()}")

#Si cada diccionario de usuario tiene diferentes llaves el codigo dentro del loop
#for se volvera mas complicado.

