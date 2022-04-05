#Crea un programa que simule como los sitios web se aseguran que cadaquien
#tiene un nombre de usuario unico.

usuarios_actuales = ['admin', 'carlos', 'daniel', 'eduardo', 'santiago']


usuarios_nuevos = ['amaranta', 'esperanza', 'brandy', 'angela', 'EDUARDO']

usuarios_nuevos_1 = usuarios_nuevos [:]

for usuario_nuevo in usuarios_nuevos_1:
	if usuario_nuevo.lower() in usuarios_actuales:
		print(f"{usuario_nuevo.title()}, busca un nuevo nombre de usuario perra!")
	else:
		print(f"{usuario_nuevo.title()}, este nombre de usuario esta disponible perra!")