#	TUPLES
#Aveces querras crear una lista de items que no pueda cambiar, tuples te ayuda a
#hacer esto Python refiere a valores que no pueden cambiar de inmutables y una 
#lista inmutable es llamada tuple.

#*Definiendo un tuple
#Luce exactamente igual a una lista, excepto que los valores estan dentro de 
#parentesis redondos y no cuadrados, el acceso a los items se hace de la misma 
#manera que en las listas por ejemplo si tenemos un rectangulo que deberia tener
#siempre determinadas medidas podemos asegurarnos de que este valor no cambiara,
#poniendo las dimensiones en un tuple:

dimensiones = (200, 50)
#print(dimensiones[0])
#print(dimensiones[1])

#veremos los que sucede si se quiere cambiar las dimensiones:

#dimensiones[0] = 250

#en este caso Python retornara un error de 'tuple', los tuples estan definidos 
#tecnicamente por una coma si quieres definir un tuple con un elemento deberas 
#agregar una coma a la cola de elementos.

#*Looping a lo largo de los valores en un tuple
#se puede hacer un loop a lo largo de un tuple asi como se hace en listas

#for dimension in dimensiones:
#	print(dimension) 

#*Escribiendo sobre un tuple
#A pesar de que no se puede modificar un tuple, si se puede asignar un nuevo 
#valor a una variable que representa un tuple, si queremos cambiar los valores 
#se puede redefinir toda la variable:

print("Dimensiones originales:")
for dimension in dimensiones:
	print(dimension) 

dimensiones = (400, 100)
print("\nDimensiones modificadas:")
for dimension in dimensiones:
	print(dimension) 
	
#no hay errores por que reasignar una nueva variable es valido
#los tuples son estructuras de informacion, se deben usar cuando se desea
#almacenar informacion que no va a cambiar a lo largo de la vida del programa

