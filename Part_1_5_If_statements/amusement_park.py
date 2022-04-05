#*Cadena if-elif-else
#A menudo querras evaluar mas de dos situaciones posibles, para hacerlo se usa 
#la sintaxis de Python if-elif-else. Python ejecuta solo un bloque en la cadena.
#corre cada test condicional hasta que uno de ellos pase. Cuando pasa, el codigo
#seguido a ese test condicional se ejecuta y se saltan los otros test.
#Considera un museo parqueadero de museo que tiene diferentes tarifas para
#diferentes grupos de edad:
#- Edades menores de 4 es gratuito.
#- Edades entre 4 y 18 es a 800.
#- Edades de 18 o mayores es a 1500.

#edad = 65

#if edad < 4:
#	print("El costo de ingreso es 0")
#elif edad < 18:
#	print("El costo de ingreso es 800")
#else:
#	print("El costo de ingreso es 1500")

#la sintaxis elif es en realidad otro test if, que corre solo siel test anterior
#falla, si ambos test fallan, Python corre el codigo del bloque else.
#El codigo puede ser escrito de manera mas concisa:

#if edad < 4:
#	costo = 0
#elif edad < 18:
#	costo = 800
#else:
#	costo = 1500

#print (f'Tu tarifa es {costo}.')

#*Usando multiples bloques elif
#Puedes usar en tu codigo los bloques elif que quieras. 
#Digamos que cualquiera de 65 o mayor paga la mitad de la tarifa regular:

#elif edad < 65:
#	costo = 1500
#else:
#	costo = 700

#print (f'Tu tarifa es {costo}.')

#*Omitiendo el bloque else
#Python no requiere un bloque else al final de la cadena if-elif. Aveces el 
#bloque else es util, otras veces es mas claro usar una declaracion elif 
#adicional que capte la condicion especifica de interes:

edad = 65
if edad < 4:
	costo = 0
elif edad < 18:
	costo = 800
elif edad < 65:
	costo = 1500
elif edad >= 65:
	costo = 700

print (f'Tu tarifa es {costo}.')

#De esta manera es mas claro que con el bloque else. Con este cambio, cada 
#bloque de codigo deberia pasar un test especifico para ser ejecutado.
#La declaracion else es una declaracion multifuncional. 
#compara cualquier condicion que no se halla comparado por algun if-elif test
#y que puede aveces inlcuir informacion invalida o maliciosa. Si tienes alguna 
#condicion especifica final que quieres testar, como resultado, aseguraras
#que tu codigo correra solo bajo las condiciones correctas.
