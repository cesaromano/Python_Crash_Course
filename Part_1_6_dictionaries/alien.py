#	DICTIONARIES
#Los diccionarios te permiten conectar piezas de informacion relacionada.
#Pueden almacenar un monto casi ilimitado de informacion
#Entender los diccionarios te permitira modelar una gran variedad de objetos
#del mundo real mas precisamente. 
#Podras crear un diccionario para representar una persona y despues almacenar 
#la cantidad de informacion que quieras acerca de esa persona.

#*Un simple diccionario
#Considera un juego mostrando aliens que tienen diferentes colores y valores de
#puntuacion:

#alien_0 = {'color': 'green', 'points': 5}

#print(alien_0['color'])
#print(alien_0['points'])

#*Trabajando con diccionarios
#Un diccionario en Python es una coleccion de pares de valores-clave. Cada 
#clave esta asociada a un valor y puedes usar la clave para acceder a su valor
#asociado, un valor clave puede ser un numero, un string, una lista u otro 
#diccionario. De hecho, puedes usar cualquier otro objeto que quieras crear en
#python como un valor en un diccionario.
#El diccionario mas sencillo tiene exactamente un par de valor-clave, como
#se ve en el ejemplo anterior.
#Este diccionario almacena una pieza de informacion acerca del alien_0,
#color del alien. El string 'color' es una clave en este diccionario, y su 
#valor asociado es'verde'.

#*Accesando a valores en un diccionario
#Para obtener el valor asociado a una clave, da el nombre del diccionario y luego
#ubica la clave dentro de un conjunto de parentesis cuadrados, como se muestra en
#el ejemplo.

#Puedes tener un numero ilimitado de pares de valores-claves en un diccionario.
#si un jugador le dispara al alien puede conocer cuantospuntos ha ganado:

#new_points = alien_0['points']
#print(f"Acabas de ganar {new_points} puntos!")

#Agregando un nuevo par de valores-clave

#Los diccionarios son estructuras dinamicas, puedes agregar nuevos pares de 
#valores-clave a un diccionario en cualquier momento:

#print(alien_0)

#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)

#*Iniciando con un diccionario vacio 
#Aveces es necesario o conveniente iniciar con un diccionario vacio y agregarle
#un nuevo item:

#alien_0 = {}

#alien_0['color'] = 'verde'
#alien_0['puntos'] = 5

#print(alien_0)

#Tipicamente usaras diccionarios vacios cuando almacenamos informacion 
#entregada por un usuario o cuando escribes un codigo que genera un largo
#numero de pares de valores-clave automaticamente.

#*Modificando valores en un diccionario
#Imagina que el alien cambia de verde a amarillo a medida que el juego progresa:

#print(f"El alien es {alien_0['color']}.")

#alien_0['color'] = 'amarillo'
#print(f"El alien de {alien_0['color']}.")

#Cambiemos ahora la posicion de un alien que puede moverse a diferentes velocidades.
#Almacenaremos un valor representando la velocidad actual del alien y despues
#la usaremos para determinar que tan lejos de la derecha el alien deberia moverse:

alien_0 = {'x_posicion' : 0, 'y_posicion' : 25, 'velocidad' : 'media'}

#print(f"Posicion original: {alien_0['x_posicion']}")

#Mueve el alien a la derecha.
#Determina que tan lejos se mueve el alien basado en su velocidad actual.

#if alien_0['velocidad'] == 'lenta':
#	incremento_x = 1
#elif alien_0['velocidad'] == 'media':
#	incremento_x = 2
#else:
#	incremento_x = 3

#La nueva posicion es la nueva posicion mas el incremento.
#alien_0['x_posicion'] = alien_0['x_posicion'] + incremento_x

#print(f"Nueva posicion: {alien_0['x_posicion']}")

#*Removiendo pares de valores-clave
#Cuando ya no queires una pieza de informacion almacenada en un diccionario
#puedes usar la declaracion del para remover completamente un par de valores-clave
#Por ejemplo, vamos a remover la vlave 'puntos' del diccionario alien_0

alien_0['puntos'] = 5
print(alien_0)

del alien_0['puntos']
print(alien_0)

