#*Usando argumentos keyword arbitrarios
#Aveces querras aceptar un numero arbitrario de argumentos, pero no querras saber
#mas adelante que tipo de informacion sera pasado a la funcion. En este caso,
#tu puedes escribir funciones que acepten los pares de valor-clave que el llamado
#de funcion provea. 
#Un ejemplo  involucra la creacion de perfiles de usuario: sabes que obtendras
#informacion acerca de un usuario, pero no sabes que tipo de informacion recibiras 
#El siguiente ejemplo toma el nombre y apellido, pero aceptando un numero arbitrario
#de argumentos keyword tambien:

def construir_perfil(nombre, apellido, **informacion_usuario):
	"""Construye un diccionario que contiene todo lo que sabemos acerca de un usuario"""
	informacion_usuario['nombre'] = nombre
	informacion_usuario['apellido'] = apellido
	return informacion_usuario

perfil_usuario = construir_perfil('albert', 'einstein', ubicacion='princeton',
	campo='fisica')

print(perfil_usuario)

#El doble asterisco antes del parametro **informacion_usuario causa que Python
#cree un diccionario vacio llamado informacion_usuario y almacene cualquier 
#par nombre-valor recibidos en el diciconario.
#La funcion podra trabajar no importa cuantas pares clave-valor sean dados en el
#llamado de funcion. 
#Puedes combinar argumentos de posicion, keyword y arbitrarios de muchas maneras
#diferentes cuando estas escribiendo tus propias funciones. 
#A menudo encontraras el nombre de parametro **kwargs usado para colectar argumentos
#keyword no especificos.

