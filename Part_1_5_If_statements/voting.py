#	IF STATEMENTS
#Existen diferentes tipos de declaraciones if, y puedes elegirlas dependiendo
#del numero de condiciones que necesites verificar.

#*Simples declaraciones if
#el tipo de declaracion simple tiene un test y una accion 
#if conditional_test:
#	do something
#puedes colocar cualquier test condicional en la primera linea y cualquier
#accion en el bloque identado.
#si el test condicional evalua True, Python ejecuta el codigo siguiendo la
#declaracion.
#El siguiente codigo prueba si una persona puede votar:
 
edad = 19

if edad >= 18:
	print("Tienes edad suficiente para votar")

#La identacion juega el mismo papel en las declaraciones if que en loop for
#Todas las lineas identadas despues de una delcaracion if seran ejecutadas
#si el test pasa, si el test no pasa todas las lineas despues de la delcaracion
#no seran ejecutadas.
#Puedes poner las lineas de codigo que quieras despues de la dclaracion if:

	print("\nYa fuiste registrado para votar?")

#Si el valor de la edad es menor de 18, el programa no generara output.

#*Declaraciones IF-else
#A menudo querrras tomar una accion cuando el test condicional pase y una accion
#diferente cuando no. La sintaxis de Python if-else lo hace posible.
#la declaracion else, te permite definir una accion o conjunto de acciones
#cuando cuando el test falla.

else: 
	print("Lo sentimos, estas demasiado pelao para votar")
	print("\nRegistrate para votar apenas hallas cumplido 18 mijo!")

#Las estructuras if-else trabajan bien en situaciones en las que quieres que 
#quieres que Python siempre ejecute una de las dos posibles acciones. En una
#simple cadena if-else como esta, una de las dos acciones siempre sera ejecutada