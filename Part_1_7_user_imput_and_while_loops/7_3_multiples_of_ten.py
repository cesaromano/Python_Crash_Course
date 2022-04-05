#Preguntale un numero al usuario y luego reportale si el numero es multiple de 
#10 o no:

numero = input("Ingresa un numero, y te dire si es multiplo de 10 o no maldito imbecil ")
numero = int(numero)

if numero % 10 == 0:
	print(f"\nEl numero {numero} es divisible chupa bolas!")
else:
	print(f"\nEl numero {numero} no es divisible pendejo!")