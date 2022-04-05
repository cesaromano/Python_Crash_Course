#*Modificando una lista en una funcion
#Cuando pasas una lista a una funcion, la funcion puede modificar la lista.
#Todos los cambios realizados a la lista dentro del cuerpo de la funcion son 
#permanentes, permitiendote trabajar eficientemente incluso cuando estas tratando
#con una gran cantidad de informacion de informacion.

#Inicia con algunos diseños que necesitan ser impresos.
#sin_imprimir = ['retenedor de telefono', 'manija', 'dedo']
#impresos = []

#Simula impresion de cada diseño, hasta que ninguno falte.
#Mueve cada diseño  a modelos_completados despues de impresos.

#while sin_imprimir:
#	impresion_actual = sin_imprimir.pop()
#	print(f"Imprimiendo modelo: {impresion_actual}")
#	impresos.append(impresion_actual)

#Muestra todas las impresiones completas
#print("\nLos siguientes modelos han sido impresos:")
#for impreso in impresos:
#	print(impreso)

#Podemos reorganizar este codigo escribiendo dos funciones, cada una haciendo un
#trabajo especifico.

def impresion_modelos(sin_imprimir[:], impresos):
	"""
	Simula impresion de cada diseño, hasta que ninguno falte.
	Mueve cada diseño  a modelos_completados despues de impresos.
	"""
	while sin_imprimir:
		impresion_actual = sin_imprimir.pop()
		print(f"Imprimiendo modelo: {impresion_actual}")
		impresos.append(impresion_actual)

def mostrar_modelos_completos(impresos):
	"""Muestra todas las impresiones completas"""
	print("\nLos siguientes modelos han sido impresos:")
	for impreso in impresos:
		print(impreso)

sin_imprimir = ['retenedor de telefono', 'manija', 'dedo']
mostrar_modelos_completos(sin_imprimir)

#Los nombres descriptivos de las funciones permiten a otros leer y entender el
#codigo. 
#Este programa es mas facil de extender y mantener que la version sin funciones.
#Si necesitamos imprimir mas diseños mas adelante, simplemente llamamos la funcion
#impresion_modelos() de nuevo. Si nos damos cuenta el codigo de impresion necesita
#ser modificado, podemos cambiar el codigo una vez, y nuestros cambios tomaran
#lugar donde quiera que la funcion sea llamada. Estatecnica es mas eficiente que
#tener que actualizar el codigo separadamente en varios lugares del programa.
#Este ejemplo tambien demuestra la idea de que cada funcion debera tener un
#trabajo especifico. La primera funcion imprime cada diseño, y la segunda muestra
#los modelos completados. Esto es mas benefico que usar una funcion para hacer 
#ambos trabajos. Si estas escribiendo una funcion y te das cuenta de que la
#funcion esta haciendo demsiados tareas, intenta cortar el codigo en dos funciones.
#recuerda que puedes llamar siempre la funcion desde otra funcion en la cual 
#puede ser de ayuda fragmentamos una tarea compleja en una serie de pasos.

#*Evitar que una funcion modifique una lista
#Aveces querras evitar que una funcion modifique una lista. En este caso podras
#abordar este problema pasando a la funcion una copia de la lista. todos los cambios
#que la funcion haga a la lista afectara solo la copia, dejando la lista original
#intacta.
#Puedes enviar una copia de una lista a una funcion de esta manera:

#nombre_funcion(nombre_lista[:])

#La notacion de slice [:] hace una copia de a lista para enviarla a la funcion.
#A pesar de que puedes preservar el contenido de una lista pasando una copia de 
#ella a tus funciones, deberias pasar la lista original a funciones a menos que 
#tengas una razon especifica para pasar una copia. Es mas eficiente para una
#funcion trabajar con una lista existente para evitar usar el tiempo y memoria
#necesarias para hacer una copia separada, especialmente cuando estas trabajando
#con listas largas.

