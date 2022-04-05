#5. IF STATEMENTS
#Programar a menudo implica examinar un conjunto de condiciones y decidir 
#cual accion tomar basada en esas condiciones. la declaracion if de Python
#te permite examinar el estado actual de un programa y responder apropiadamente
#a ese estado.

#	A SIMPLE EXAMPLE
#El siguiente ejemplo muestra como la declaracion if te permite responder a 
#situaciones especiales correctamente. Por ejemplo imprimiendo solamente un 
#item de una lista en mayuscula:

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#El loop en el ejemplo, primero verifica si el valor actual es 'bmw', si es asi
#el valor es impreso en mayuscula, si no es asi solo es impreso con la primera
#letra en mayuscula.

#	TEST CONDICIONALES
#El corazon de cada declaracion if es una expresion que puede ser evaluada como
#True o False y es llamada un Test Condicional. Python usa los valores True and
#False para decidir si el codigo dentro de una declaracion if deberia ser 
#ejecutada. Si el test condicional evalua True, Python ejecuta el codigo 
#siguiendo la declaracion if. Si el test evalua False, Python ignora el codigo 
#siguiendo la declaracion if.

#*Verificando la igualdad
#La mayoria de tests condicionales comparan el valor actual de una variable para
#un valor de interes especifico. El simple test condicional verifica si el valor
#de la variable es igual para el valor de interes:

#>>> car = 'bmw'
#>>> car == 'bmw'
#True

#si el valor de la variable coincide con el valor del test, Python entrega True

#>>> car = 'audi'
#>>> car == 'bmw'
#False

#si el valor de la variable no coincide con el valor del test, Python entrega 
#False.

#Un simple valor de igual es en realidad una declaracion que ajusta el valor de
#carro igual a 'audi'. Por otro lado, un signo de doble igual realiza la 
#pregunta: "es el valor de carro igual a 'bmw'?", la mayoria de lenguajes de
#programacion usa los signos de igual de esta manera.

#*Ignorando el formato cuando se verifica la igualdad
#Las pruebas de igualdad de Python distinguen entre mayusculas y minusculas.
#por ejemplo, dos valores con diferente formato no son consideradas iguales

#>>> car = 'Audi'
#>>> car == 'audi'
#False

#si el formato importa, este comportamiento es ventajoso. Pero si el formato no
#importa y en cambio solo quieres verificar el valor de la variable, puedes 
#convertir el valor de la variable a minuscula antes de hacer la comparacion:

#>>> car = 'Audi'
#>>> car.lower() == 'audi'
#True

#La funcion lower() no afecta la variable original, asi que se puede hacer esta 
#comparacion para sin afectar la variable original.

#Muchos sitios web utilizan estos test de comparacion para asegurarse de que 
#cada  usuario tenga un nombre de usuario unico y verdadero, no solo una 
#variacion en el formato del nombre de usuario de otra persona.