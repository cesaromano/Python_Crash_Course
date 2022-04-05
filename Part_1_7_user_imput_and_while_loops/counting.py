#	INTRODUCIENDO LOOPS WHILE
#Un loop for toma una coleccion de items y ejecuta un bloque de codigo una vez
#por cada item en la coleccion. En contraste, el loop while corre tanto como, o
#mientras, una cierta condicion es verdadera.

#*El loop while en accion
#Puedes usar un loop while para contar a lo largo de una serie de numeros.
#Por ejemplo, el siguiente loop while cuenta de 1 a 5:

#numero_actual = 1
#while numero_actual <=5:
#	print(numero_actual)
#	numero_actual += 1

#la expresion (numero_actual += 1) es una abreviacion de (numero_actual = 
#numero_actual + 1)
#Python repite el loop hasta que hasta que la condicion sea verdadera.
#La mayoria de programas que usas a diario contienen loops while.Por ejemplo,
#un juego necesita un loop while para mantenerse corriendo tanto como quieras
#mantenerte jugando, y en cuanto queiras parar de correrlo buscar salir.

#*Usanco continue en un loop
#Puedes usar la declaracion "continue" para volver al comienzo del loop basado
#en el resultado de un test condicional. 
#Por ejemplo, considera un loop que cuente de 1 a 10 pero que imprima solo los
#numeros impares en ese rango:

#numero_actual = 0
#while numero_actual < 10:
#	numero_actual += 1
#	if numero_actual % 2 == 0:
#		continue

#	print(numero_actual)

#La declaracion continue le dice a python que ignore el resto del loop y vuelva
#al principio, si el numero actual no es divisible por dos,el resto del loop es
#ejecutado y python imprime el numero actual.

#*Evitando loops infinitos
#Cada loop while necesita una forma de parar de correr de manera que no siga
#corriendo para siempre.
#Por ejemplo, este loop cuenta los numeros de 1 a 5:

#x = 1
#while x <= 5:
#	print(x)
#	x += 1

#Pero si accidentalmente omites la linea x += 1, el loop correra para siempre:

x = 1
while x <= 5:
	print(x)
	
#Si tu programa se queda estancado en un loop infinito presiona CTRL-C.
#Para evitar escribir loops infinitos, prueba cada loop y asegurate que el loop
#pare cuando desees que lo haga.

