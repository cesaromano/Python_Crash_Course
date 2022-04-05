#Inicia con el ejercicio que escribiste en 6_1:

persona_0 = {
	'nombre' : 'sergio',
	'apellido' : 'garcia',
	'edad' : 13,
	'ciudad' : 'bogota',
}

#Haz dos nuevos diccionarios representando personas diferentes:

persona_1 = {
	'nombre' : 'romano',
	'apellido' : 'delgado',
	'edad' : 24,
	'ciudad' : 'bogota',
}

persona_2 = {
	'nombre' : 'lucas',
	'apellido' : 'yoshin',
	'edad' : 26,
	'ciudad' : 'bucharest',
}

#almacena todos los tres diccionarios en una lista llamada personas:

personas = [persona_0, persona_1, persona_2]

#has un loop a lolargo de la lista de personas, imprime todo lo que sabes
#sobre cada persona:

for persona in personas:
	print(persona)

#for persona in personas:
#	print(f"\n{persona}:")
#	for item, informacion in persona.items():
#		nombre_completo = f"{item['nombre']} {item['apellido']}"
#		edad = f"{item['edad']}"
#		ciudad = f"{item['ciudad']}"

#		print(f"\tNombre: {nombre_completo.title()}")
#		print(f"\tEdad: {edad}")
#		print(f"\tCiudad: {ciudad.title()}")
