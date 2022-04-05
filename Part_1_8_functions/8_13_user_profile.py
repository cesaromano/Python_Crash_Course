#inicia con una copia de user_profile.py, construye un perfil tuyo por medio del 
#llamado de funcion usando tu nombre y apellido y otros tres pares de clave_valor
#que te describan

def construir_perfil(nombre, apellido, **informacion_usuario):
	"""Construye un diccionario que contiene todo lo que sabemos acerca de un usuario"""
	informacion_usuario['nombre'] = nombre
	informacion_usuario['apellido'] = apellido
	return informacion_usuario

perfil_usuario = construir_perfil('romano', 'delgado', ubicacion='bogotá',
	campo='educacion en tecnologia', edad= 24, ambicion= 'el mundo', amor= 'propio')

print(perfil_usuario)