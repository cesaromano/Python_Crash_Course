#	ANIDANDO
#Aveces necesitaras almacenar multiples diccionarios en una lista, o una lista
#de items como un valor en un diccionario. A esto se le llama anidar. Puedes
#anidar diccionarios en una lista, una lista de items dentro de un diccionario
#o un diccionario dentro de otro diccionario. Anidar es una poderosa caracteristica.

#*Una lista de diccionarios
#El diccionario alien_0 contiene una variedad de informacion acerca de un alien
#pero no hay espacio para almacenar informacion acerca de un segundo alien,
#mucho menos una pantalla llena de aliens. Como puedes manejar una flota de aliens?
#Una manera es hacer una lista de aliens en la cual cada alien es un diccionario
#de informacion acerca de ese alien. Por ejemplo, el siguiente coodigo construye
#una lista de tres aliens:

#alien_0 = {'color' : 'green', 'puntos' : 5}
#alien_1 = {'color' : 'amarillo', 'puntos' : 10}
#alien_2 = {'color' : 'rojo', 'puntos' : 15}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#	print(alien)

#El siguiente ejemplo usa la funcion range() para crear una flota de 30 aliens:

#Primero se hace una lista vacia para almacenar los aliens.
#aliens = []

#se crean los 30 aliens.
#for numero_alien in range(30):
#	nuevo_alien = {'color' : 'verde', 'puntos' : 5, 'velocidad' : 'baja'}
#	aliens.append(nuevo_alien)

#imprimiendo los primeros 5 aliens.
#for alien in aliens[:5]:
#	print(alien)
#print("...")

#mostrando cuantos aliens se han creado.
#print(f"El numero total de aliens creados es: {len(aliens)}")

#Imagina que uno de los aspectos del juego tiene algunos aliens cambiando de 
#color y moviendose rapidamente a medida que el juego progresa. Cuando sea tiempo
#de cambiar de colores podemos usar un loop for y una declaracion if para cambiar
#el color de los aliens. Por ejemplo, para cambiar los tres primeros aliens a 
#amarillo, velocidad media y puntaje 10, podriamos hacer lo siguiente:

#for alien in aliens[:3]:
#	if alien['color'] == 'verde':
#		alien['color'] = 'amarillo'
#		alien['velocidad'] = 'media'
#		alien['puntos'] = '10'
	

#for alien in aliens[:5]:
#	print(alien)

#Puede expandirse el codigo añadiendo un codigo elif que cambie los aliens 
#amarillos a rojos, velovidad alta y puntaje 15. Sin mostrar el programa entero 
#otra vez, el loop puede lucir de esta menra:

#elif alien['color'] == 'amarillo':
#		alien['color'] = 'rojo'
#		alien['velocidad'] = 'alta'
#		alien['puntos'] = 15

#Es comun almacera un numero de diccionarios en una lista cuando cada diccionario
#contiene muchos tipos de informacion acerca de un objeto. Por ejemplo, puedes
#crear un diccionario por cada usuario en un sitio web, y almacenar los diccionarios
#individuales en una lista de usuarios. Todos los diccionarios en la lista tienen
#deberian tener una estructura identica asi tu puedes hacer loop a lo largo de 
#la lista y trabajar con cada diccionario objeto de la misma manera.