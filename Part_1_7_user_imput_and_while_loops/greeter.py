#*Escribir prompts claros
#Cada vez que uses la funcion input(), deberias incluir un claro y facil de seguir
#prompt que le diga al usuario exactamente que tipo de informacion necesitas
#Por ejemplo:

#nombre = input("\nPor favor ingresa tu nombre: ")
#print(f"\nHola, {nombre}!")

#Agrega espacioal finalizar tus prompts despues de los dos puntos.
#A veces querras escribir un prompt que es mas largo que una linea. 
#Por ejemplo, podrias querer decirle al usuario por que estas necesitando dicha
#informacion. Puedes asignar tu prompt a una variable y pasar esa variable a la
#funcion imput(). Esto te permitira construir tu prompt en varias lineas, despues
#escribir una declaracion input() clara.

prompt = "Si nos dices quien eres, podemos personalizar los mensajes que ves."
prompt += "\nCual es tu primer nombre? "

nombre = input(prompt)
print(f"\nHola, {nombre}!")

#Este ejemplo muestra una manera de construir un string multilinea

#*Usando int() para aceptar input numerico
#La funcion input() interpreta cualquier cosa que el usuario ingrese como un 
#string. Por ejemplo:

#>>> edad = input("Cuantos años tienes? ")
#Cuantos años tienes? 24
#>>> edad
#'24'

#Cuando el usuario ingresa el valor, python regresa '24', la representacion en 
#string del valor numerico. Si lo unico que quieres es imprimir el inut, este 
#codigo funcionara bien, pero si intentas usar el imput como un numero, tendras
#un gran error:

#>>> edad = input("Cuantos años tienes? ")
#Cuantos años tienes? 24
#>>> edad >= 18
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: '>=' not supported between instances of 'str' and 'int'

#Esto sucede por que Python no puede comparar un string con un entero.
#podemos resolver este error usandola funcion int(), que le dice a Python que 
#trate el input como un valor numerico. La funcion int() convierte una represen
#tacion de string a una representacion numerica, como se muestra aqui:

#>>> edad = input("Cuantos años tienes? ")
#Cuantos años tienes? 24
#>>> edad = int(edad)
#>>> edad >= 18
#True

#El valor es convertido a una representacion numerica con la funcion int()