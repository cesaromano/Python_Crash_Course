import module_privileges as mp

administrador = mp.Admin('Romano', 'Delgado', 24, 'Masculino')
#administrador.greet_user()
#administrador.describe_user()
administrador.privilegess.show_privileges()

#	THE PHYTON STANDART LIBRARY
#Es un conjunto de modulos incluidos con cada instalacion de Phyton
#Puedes usar cualquier funcion o clase en la libreria standard incluyendo
#una simple declaracion "import" al comienzo del archivo. Veamos el
#modulo "random". Una funcion interesante del modulo random es 
#randint(). Esta funcion toma dos enteros como argumentos y retorna
#un numero al azar entre los dos numeros.

#>>> from random import randint
#>>> randint(1, 6)
#2

#Otra funcion util es choice(). Esta funcion toma de una lista o
#tuples y retorna un elemento al azar

#>>> from random import choice
#>>> players = ['charles', 'martina', 'michael', 'florence', 'eli']
#>>> first_up = choice(players)
#>>> first_up
#'charles'

#El modulo random no deberia ser usado cuando se construyen aplicacio
#ones relacionadas con seguridad, pero es buena para muchos interesantes
#y divertidos proyectos
#Puedes tambien descargar modulos de fuentes externas. Veras un numero
#de esos ejemplos en Part II, donde necesitaremos modulos externos para
#completar cada proyecto.