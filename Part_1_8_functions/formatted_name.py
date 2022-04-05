#	RETORNANDO VALORES
#El valor que una funcion retorna se llama "return value". La declaracion
#"return" toma un valor dentro de la funcion y lo envia de vuelta a la linea
#que llamo la funcion. Retornar valores te permite mover mucho del trabajo
#monotono de los programas en las funciones, el cual puede simplificar el cuerpo
#de tu programa.

#*Retornando un simple valor

#def dar_formato_nombre(nombre, apellido):
#	"""Retorna un nombre completo, con formato claro"""
#	nombre_competo = f"{nombre} {apellido}"
#	return nombre_competo.title()

#musico = dar_formato_nombre('victor', 'garcia')
#print(musico)

#Esto se ve como mucho trabajopara obtener un nombre con formato claro, pero
#cuando consideras trabajar con un gran programa que necesita almacenar muchos
#nombres y apellidos separadamente, funciones como esta se vuelven muy utiles.
#Almacenas nombre y apellido separadamente y luego llamas la funcion donde 
#deseas mostrar el nombre completo.

#*Haciendo un argumento opcional
#Aveces tiene sentido hacer un argumento opcional de modo tal que las pereonas 
#usando la funcion puedan elegir la informacion extra que proveen. Puedes usar
#valores por defecto para hacer un argumento opcional.

#def dar_formato_nombre(nombre, segundo_nombre, apellido):
#	"""Retorna un nombre completo, con formato claro"""
#	nombre_competo = f"{nombre} {segundo_nombre} {apellido}"
#	return nombre_competo.title()

#musico = dar_formato_nombre('victor', 'manuel', 'garcia marin')
#print(musico)

#Esta funcion trabaja cuando se dan los tres argumentos. 
#Pero los segundos nombres no siempre son necesarios. Para hacer el segundo 
#nombre opcional, podemos dar el argumento del segundo_nombre como valor por
#defecto vacio a no ser que el usuario provea el vallor.

def dar_formato_nombre(nombre, apellido, segundo_nombre= ''):
	"""Retorna un nombre completo, con formato claro"""
	if segundo_nombre:
		nombre_competo = f"{nombre} {segundo_nombre} {apellido}"
	else:
		nombre_competo = f"{nombre} {apellido}"
	return nombre_competo.title()

musico = dar_formato_nombre('victor', 'garcia marin')
print(musico)

musico = dar_formato_nombre('victor', 'manuel', 'garcia marin')
print(musico)

#Valores opcionales le permite a las funciones manejar un gran rango de casos 
#mientras les permite a las funciones de llamada permaneces tan simples como
#es posible.