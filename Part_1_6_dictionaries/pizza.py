#*Una lista en un diccionario
#A veces es util poner una lista en un diccionario. Por ejemplo, considera como
#podrias describir una pizza que alguien ordeno. Si usaras solo una lista, todo
#lo que podrias realmente almacenar es una lista de las adiciones de la pizza. 
#Con un diccionario, una lista de adiciones puede ser solo un aspecto de la pizza
#que estas describiendo.
#En el siguiente ejemplo, dos tipos de informacion son almacenados para cada
#pizza: un tipo de corteza y una lista de adiciones. La lista de adiciones es un
#valor asociado a la llave 'adiciones'. Para usar los items en la lista dimos
#el nombre del diccionario y y la llave 'adiciones'. En vez de retornar un simple
#valor, tenemos una lista de adiciones:

#Almacenando informcion de una pizza que ha sido ordenada.
#pizza = {
#	'corteza' : 'delgada',
#	'adiciones' : ['champiñones', 'queso extra'],
#}

#Totalizando la orden
#print(f"Ordenaste una pizza con corteza {pizza['corteza']}"
#	" y las siguientes adiciones:")

#for adicion in pizza['adiciones']:
#	print(f"\t{adicion}")