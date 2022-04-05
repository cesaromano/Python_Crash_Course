#	TRABAJANDO CON UNA PARTE DE UNA LISTA
#Trabajo con un grupo especifico de elementos al que Python
#denomina "slice"

#*Slicing a list 
#Para hacer un slice especifica el indice del primero y ultimo elementos
#con los que deseas trabajar, de igual manera que la funcion range()
#python se detiene un elemento antes del segundo indice especificado
#jugadores = ['juan', 'gerson', 'brandon', 'kate', 'alejo', 'angy']
#print(jugadores[0:3])
#el rango en la segunda linea del codigo es el slice 
#como salida se obtiene la misma estructura de la lista 
#incluyendo los tres primeros items
#se puede obtener cualquier subconjunto de la lista
#print(jugadores[0:4])
#si se omite el primer indice, python automaticamente inicia desde el primer item
#print(jugadores[:4])
#ocurre de manera similar si se omite el segundo indice, tomando como segundo indice el item final de la lista
#print(jugadores[2:])
#llamando un indice negativo tomara el valor del indice con sentido del final de la lista al inicio 
#por ejemplo, para llamar a los ultimos 3 jugadores
#print(jugadores[-3:])
#incluyendo un tercer argumento le dira a python el numero de items que excluir entre elemento y elemento
#print(jugadores[0:4:2])

#*Looping en un slice
#se puede usar un slice en un loop for
jugadores = ['juan', 'gerson', 'brandon', 'kate', 'alejo', 'angy']

print("Estos son los tres primeros jugadores de mi equipo:")
for jugador in jugadores [:3]:
	print(jugador.title())
#en vez de hacer un loop a lo largo de toda la lista, python solo hace un loop en ese slice
#esto es muy util en un video juego para agregar los puntajes finales de un jugador cada vez que termine de jugar
#se podrian obtener los tres mejores puntajes ordenando la lista de mayor a menor y obteniendo la porcion de los tres primeros puntajes
#trabajando con informacion se pueden usar slices para procesar la informacion en porciones de un tamaño especifico
#o cuando se construye una aplicacion web, se pueden usar slices para mostrar informacion en una serie de paginas con un
#apropiado monto de informacion en cada pagina