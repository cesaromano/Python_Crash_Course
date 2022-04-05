#Has varios diccionarios, donde cada diccionario representa una mascota diferente
#en cada diccionario incluye el tipo de animal y el nombre del dueño 

mascota_0 = {
	'tipo de animal' : 'perro',
	'dueño' : 'romano',
}

mascota_1 = {
	'tipo de animal' : 'serpiente',
	'dueño' : 'david',
}

mascota_2 = {
	'tipo de animal' : 'gorilla',
	'dueño' : 'victor',
}

mascota_3 = {
	'tipo de animal' : 'gato',
	'dueño' : 'mabo',
}

mascotas = [mascota_0, mascota_1, mascota_2, mascota_3]

for mascota in mascotas:
	print(mascota)

