#*Verificando una desigualdad
#Para verificar si dos valores no son iguales se usa la siguiente combinacion
#de signos (!=). El signo de exclamacion representa un no.

#aderezo_requerido = 'hongos'

#if aderezo_requerido != 'anchoas':
#	print('Deja las anchoas')

#La mayoria de las expresiones condicionales que escribes probaran igualdades
#pero aveces encontraras mas eficiente provar desigualdades.

#* Testando multiples condiciones
#La cadena if-elif-else es muy poderosa pero solo es apropiada cuando necesitas
#un solo test para pasar.Una vez que Python encuentra un test que pase, 
#dejara los demas test. 
#Sin embrgo aveces es importante verificar todas las condiciones de interes. 
#En este caso, deberas usar series de declaraciones if sin bloque elif-else.
#Si alguien requiere dos adiciones de pizza, necesitaras asegurarte de incluir
#ambas adiciones en su pizza:

#adicion_requerida = ['champiñones', 'queso extra']

#if 'champiñones' in adicion_requerida:
#	print("Agrega champiñones.")
#if 'jamon' in adicion_requerida:
#	print("Agrega jamon.")
#if 'queso extra' in adicion_requerida:
#	print("Agrega queso extra.")

#print("\n Pizza acabada!")

#Este codigo puede no funcionar correctamente si usamos un bloque if-elif-else
#por que el codigo parara una vez que uno de los test pase:

#adicion_requerida = ['champiñones', 'queso extra']

#if 'champiñones' in adicion_requerida:
#	print("Agrega champiñones.")
#elif 'jamon' in adicion_requerida:
#	print("Agrega jamon.")
#elif 'queso extra' in adicion_requerida:
#	print("Agrega queso extra.")

#print("\n Pizza acabada!")

#El test para champiñones fue el primero en pasar, de tal modo que los champiñones
#fueron agregados a la pizza. Sin embargo los valores 'extra queso' y 'jamon'
#jamas fueron evaluados.
#En resumen, Si quieres un solo bloque de programa para correr, usa la cadena
#if-elif-else. Si mas de un bloque debe de programa debe ser corrido, usa
#series de declaraciones if independientes.

#	USANDO DECLARACIONES IF EN LISTAS
#Puedes buscar valores especificos para tratarlos de manera diferente a otros.
#Puedes manejar condiciones cambiantes eficientemente, como la disponiblidad
#de ciertos items en un restaurante a lo largo de un cambio.

#*Verificando items especiales
#Veamos mas de cerca como encontrar valores especiales en una lista y manejar
#esos valores apropiadamente.
#Continuemos con el ejemplo de la pizzeria. La pizzeria muestra un mensaje 
#siempre que una adicion es agregada a tu pizza. El codigo para esta accion
#puede ser escrito muy eficientemente haciendo una lista de adiciones que el
#usuario ha pedido y usando un loop para anunciar que cada adicion ha sido
#agregada a la pizza:

#adiciones_requeridas = ['champiñones', 'pollo', 'chile', 'piña']

#for adicion_requerida in adiciones_requeridas:
#	print(f"Agregando {adicion_requerida}.")

#print("\nPizza realizada! ")

#Pero que pasaria si la pizza se quedara sin chile?, Una declaracion if 
#podria manejar esta situacion apropiadamente

#adiciones_requeridas = ['champiñones', 'pollo', 'chile', 'piña']

#for adicion_requerida in adiciones_requeridas:
#	if adicion_requerida == 'chile':
#		print("Lo lamentamos, los chiles se encuentran agotados en este momento.")
#	else:
#		print(f"Agregando {adicion_requerida}.")



#print("\nPizza realizada! ")

#*Verificando que una lista no esta vacia
#Asumimos que cada lista con la que trabajamos tiene al menos un item.
#Es util verificar si una lista esta vacia antes de correr un loop.
#Verifiquemos si la lista de adiciones requeridas esta vacia antes de construir
#la pizza.

#adiciones_requeridas = []

#if adiciones_requeridas:
#	for adicion_requerida in adiciones_requeridas:
#		print(f"Agregando {adicion_requerida}.")
#	print("\n Pizza realizada")

#else:
#	print("Estas seguro de que no quieres adiciones en tu pizza?")

#Cuando el nombre de la lista es usado en una declaracion if, Python retorna
#True si la lista contiene al menos un item; una lista vacia retorna False.

#*Usando multiples variables
#Que pasa si un usuario quiere papas fritas en su pizza? Puedes usar listas
#y declaraciones if.
#Veamos adiciones requeridas inusuales antes de que construyamos nuestra pizza
#la primera es una lista de adiciones disponibles en la pizzeria, y la 
#segunda es la lista de adiciones que el usuario ha solicitado.
#En esta ocacion, cada item en adiciones requeridas es verificado en la lista de
#adiciones disponibles antes de ser agregada a la pizza:

adiciones_disponibles = ['champiñones', 'aceitunas', 'pimientos verdes', 'jamon',
						'piña', 'queso extra']

adiciones_requeridas = ['champiñones', 'papas fritas', 'queso extra']

for adicion_requerida in adiciones_requeridas:
	if adicion_requerida in adiciones_disponibles:
		print(f"Agregando {adicion_requerida}.")
	else:
		print(f"Lo sentimos, a quien carajos se le ocurre poner {adicion_requerida} en una pizza?")

print("\n Pizza finalizada")



