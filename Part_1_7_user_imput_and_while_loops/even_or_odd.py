#Cuando un numero es divisible por otro numero, el residuo es 0, asi que el 
#operador del modulo es 0, puedes usar este principio para determinar si un numero
#es par o impar:

numero = input("Ingresa un numero, y te dire si es par o impar maldito imbecil ")
numero = int(numero)

if numero % 2 == 0:
	print(f"\nEl numero {numero} es par chupa bolas!")
else:
	print(f"\nEl numero {numero} es impar pendejo!")

#Los numeros pares son siempre divisibles por dos, de tal manera que si el
#modulo es 0 el numero es par. De otro modo es impar.

