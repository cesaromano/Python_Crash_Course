#Almacena los numeros del 1 al 9 en una lista

numeros = list(range(1, 10))

for numero in numeros:
	if numero == 1:
		print(f"\n {numero}st")
	elif numero == 2:
		print(f"\n {numero}nd")
	elif numero == 3:
		print(f"\n {numero}rd")
	elif numero > 3:
		print(f"\n {numero}th")


