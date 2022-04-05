#*Comparaciones numericas

#Al testar valores numericos es bastante claro. 

#>>> edad = 18
#>>> edad == 18
#True

#Tambien puedes provar para ver si dos numeros no son iguales. 

answer = 17

if answer != 42:
	print('Esa no es la respuesta correcta ome. intentalo de nuevo ñoñi')

#Puedes incluir varias comparaciones matematicas, como menor que, menor o igual
#que, mayor que, mayor o igual que:

#>>> edad = 18
#>>> edad == 18
#True
#>>> edad = 19
#>>> edad < 21
#True
#>>> edad <= 21
#True
#>>> edad > 21
#False
#>>> edad >= 21
#False

#Cada comparacion matematica puede ser usada en una declaracion if, esto puede 
#ayudar a detectar condiciones de interes.

#*Verificando condiciones multiples

#Aveces podras necesitar que dos conciones sean ciertas para tomar una accion.
#otras veces solo sera necesaria una las palabras clave and y or pueden ayudar
#en esta situacion.

#**Usando and para verificar multiples condiciones

#Para verificar si dos condiciones son ambas verdaderas simultaneamente se usa 
#and, si cada verificacion pasa la expresion general se evalua como True. Si
#una de las verificaciones o ambas fallan, la exprecion evalua False.

#>>> edad_0 = 22
#>>> edad_1 = 18
#>>> edad_0 >= 21 and edad_1 >= 21
#False
#>>> edad_1 = 22
#>>> edad_0 >= 21 and edad_1 >=21
#True

#si quieres mejorar la legibilidad, puedes usar parentesis al rededor de los 
#test individuales:

#(edad_0 >= 21) and (edad_1 >=21)

#**Usando or para verificar multiples condiciones
#or tambien permite verificar multiples condiciones, pero pasa si una 
#sola o ambos de los test individuales pasan. Una expresion or falla solo cuando
#ambos tests individuales fallan:

#>>> edad_0 =22
#>>> edad_1 =18
#>>> edad_0 >= 21 or edad_1 >=21
#True
#>>> edad_0 = 18
#>>> edad_0 >= 21 or edad_1>= 21
#False

#*Verificando si un valor esta en una lista

#Aveces es importante verificar si hay cierto valor en una lista para tomar
#una accion. 
#Por ejemplo, para verificar si un nombre de usuario ya existe para antes de 
#completar un registro en un sitio web.
#En un proyecto de mapeo,para verificar si una ubicacion entregada ya existe.
#Para verificar si un valor particular ya se encuentra en una lista se usa in.

#>>> aderezos_requeridos = ['champiñones', 'cebolla', 'piña']
#>>> 'champiñones' in aderezos_requeridos
#True
#>>> 'jamon' in aderezos_requeridos
#False

#La palabra in le dice a Python que verifique la existencia del item en la
#lista.



