#	PASANDO UN NUMERO ARBITRARIO DE ARGUMENTOS
#Aveces no sabras cuantos argumentos una funcion necesitara aceptar mas adelante
#en el tiempo. Afortunadamente, Python le permite a la funcion colectar un numero
#arbitrario de argumentos desde la funcion llamada.
#Por ejemplo, considera una funcion que construya una pizza. Necesita aceptar un
#numero de toppings, pero no puedes saber mas adelante cuantos toppings querra la
#persona. La funcion en el siguiente ejemplo tiene un parametro, *toppings,
#pero este parametro recolecta todos los argumentos que la funcion llamada proporcione:

#def hacer_pizza(*toppings):
#	"""Imprime la lista de toppings que seran solicitados"""
#	print(toppings)

#hacer_pizza('pepperoni')
#hacer_pizza('champiñones', 'pimientos', 'queso extra')

#El asteriscco en el nombre del parametro *toppings le dice a Python que haga un 
#tuple vacio llamado toppings y empaquete el valor que sea que reciba en el tuple
#El llamado en el cuerpo de la funcion produce un output mostrando que Python 
#puede manejar un llamado de funcion con un valor y un llamado con tres valores.
#Nota que Python almacena los argumentos en un tupple, incluso si la funcion recibe
#solo un valor.
#Ahora podemos reemplazar el llamado con un loop que corra por la lista de toppings
#y describa la pizza que ha sido ordenada.

#def hacer_pizza(*toppings):
#	"""Resume la pizza que vamos a hacer"""
#	print("\nHaciendo una pizza con los siguientes toppings:")
#	for topping in toppings:
#		print(f" - {topping}")

#hacer_pizza('pepperoni')
#hacer_pizza('mushrooms', 'green peppers', 'extra cheese')

#La funcion responde apropiadamente, si recibe un valor o tres.
#la sitnaxis trabaja sin importar cuantos argumentos recibe la funcion.

#*Mezclando argumentos posicionales y arbitrarios
#Si  quieres que una fucnion acepte diferentes tipos de argumentos, el parametro 
#que acepte un numero arbitrario de argumentos debe estar ubicado al final de la
#definicion de la funcion. Python seleccionara argumentos posicionales y 
#por palabras clave primero y luego colecta cualquier argumento restante al final
#del aprametro.

def hacer_pizza(tamaño, *toppings):
	"""Resume el pedido de la pizza"""
	print(f"\nHciendo una pizza de {tamaño}cm con los siguientes toppings:")
	for topping in toppings:
		print(f"- {topping}")

#hacer_pizza(30, 'pepperoni')
#hacer_pizza(25, 'mushroom', 'green peppers', 'extra cheese')

#A menudo encontraras el parametro generico *args, el cual colecta argumentos
#posicionales arbitrarios como este.

