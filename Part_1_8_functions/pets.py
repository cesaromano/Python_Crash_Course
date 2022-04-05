#	PASANDO ARGUMENTOS
#Puedes pasar argumentos a tus funciones de multiples maneras. Puedes usar 
#argumentos posicionales los cuales deben estar en el mismo orden en el que los
#parametros fueron escritos; keyword arguments, donde cada argumento consiste 
#en un nombre y valor de una variable; y listas y diccionarios de los valores.

#*Positional arguments
#Cuando llamas una funcion, Python debe coincidir cada argumento en la funcion
#llamada con un parametro en la definicion de la funcion. La forma mas facil de
#hacer esto es basado en el orden delos argumentos proveidos. Los valores 
#coincididos de esta manera son llamados positional arguments.

#def descripcion_mascota(tipo_mascota, nombre_mascota):
#	"""Muestra informacion acerca de la mascota"""
#	print(f"\nTengo un {tipo_mascota}.")
#	print(f"Mi {tipo_mascota} se llama {nombre_mascota.title()}")

#descripcion_mascota('perro', 'mambo')

#**Multiples llamados de funcion
#Puedes llamar una funcion cuantas veces sea necesario. 

#descripcion_mascota('ballena','wallie')

#llamar una fucnion multiples veces es una forma muy eficiente de trabajar. 
#Puedes usar todos los argumentos posicionales que necesites en una funcion.
#Python trabaja por medio de los argumentos que entregaste cuando llama la
#funcion y empareja cada uno con el correspondiente parametro en la definicion 
#de la funcion.

#*El orden importa en los argumentos posicionales
#Puedes obtener resultados inesperados si mezclas el orden de los argumentos en un
#llamado de funcion cuando usas argumentos posicionales. 

#descripcion_mascota('harry', 'hamster')

#*Keyword arguments
#Un keyword argument es un par de nombre-valor que pasas a una funcion. Directamente
#asocias el nombre y el valor dentro del argumento, de tal manera que cuando pasas
#el argumento a la funcion, no hay confusion. 

#descripcion_mascota(tipo_mascota='hamster', nombre_mascota='harry')

#Cuando llamamos la funcion, explicitamente le decimos a python que parametro con
#que argumento debera coincidir. Cuando Python lee la funcion, sabe como asignar
#el argumento con el parametro, el orden del keyword no importa por que Python 
#conoce donde deberia ir cada valor 

#*Default values
#Puedes definir valores por defecto para cada parametro. Si un argumento para 
#un parametro es proveido  en la funcion llamada, Python usa el valor del 
#argumento. Si no, usara el parametro del valor por defecto. Usar valores por
#defecto puede simplificar tus funciones llamadas y clarificar las formas en las
#cuales tus funciones son tipicamente usadas.

def descripcion_mascota(nombre_mascota, tipo_animal='perro'):
	"""Muestra informacion sobre mascotas"""
	print(f"\nTengo un {tipo_animal}")
	print(f"El nombre de mi {tipo_animal} es {nombre_mascota.title()}")

#descripcion_mascota(nombre_mascota='fujin')

#Nota que el orden de los parametros en la funcion tuvo que ser cambiado. Por que
#el valor por defecto hace innecesario especificar el tipo de animal, el unico
#argumento restante en la funcion llamada es el nombre de la mascota. Python
#continua intepretando esto como un argumento posicional, asi que si la funcion
#es llamada con solo el nombre de la mascota, ese argumento se emparejara con el
#primer parametro listado en la definicion de la funcion. 
#la manera mas simple de usar esta funcion ahora es proveer solo el nombre de
#la mascota:

descripcion_mascota('fujin')

#Para describir un animal diferente a un perro, puedes usar un llamado de funcion
#diferente

descripcion_mascota(nombre_mascota='fujin', tipo_animal='lagarto')

#Como fue puesto un argumento para tipo de animal en el llamado de la funcion, 
#Python ignora el valor por defecto de los parametros.

#*Llamado de funcion equivalente
#Debido a que argumentos posicionales, keyword arguments, y valores por defecto 
#pueden ser todos usados juntos, a menudo tendras varias maneras equivalentes 
#para llamar una funcion.

#Un lagarto llamado fujin
descripcion_mascota('fujin')
descripcion_mascota(nombre_mascota= 'fujin')

#Un hamster llamado bolas
descripcion_mascota('bolas', 'hamster')
descripcion_mascota(nombre_mascota= 'bolas', tipo_animal= 'hamster')
descripcion_mascota(tipo_animal= 'hamster', nombre_mascota= 'bolas')

#No importa cual estilo uses. Siempre que tu funcion llamada produsca el output
#que desees, solo usa el estilo que encuentres mas facil de entender.

#Evitando errores en argumentos
#Argumentos no coincidentes ocurre cuando provees menos o mas argumentos de los que
#una funcion necesita para hacer su trabajo.

descripcion_mascota()
#Python reconoce que falta informacion de la funcion llamada y el traceback nos lo
#menciona.




