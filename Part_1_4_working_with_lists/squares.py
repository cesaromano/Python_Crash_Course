#se puede crear casi cualquier conjunto de numeros que se desee con la funcion range()
#por ejemplo, una lista de el cuadrado de cada uno de los numeros del 1 al 10
#cuadrados = [] 
#for valor in range(1, 11):
#	cuadrado = valor**2
#	cuadrados.append(cuadrado)
#print(cuadrados)
#para hacer este codigo de manera mas consisa de hace de la siguiente manera
#cuadrados = []
#for valor in range(1, 100):
#	cuadrados.append(valor**2)
#print(cuadrados)

#*Estadisticas simples con una lista de numeros
#Unas cuantas funciones son de ayuda cuando queremos trabajar con 
#para hallar el minimo en una lista de numeros se usa la funcion min()
#digitos = []
#for digito in range(1, 11):
#	digitos.append(digito)
#print(min(digitos))
#para halllar el maximo de una lista de numeros se usa la funcion max()
#digitos_max = []
#for digito in range(1, 11):
#	digitos_max.append(digito)
#print(max(digitos))
#para hallar la suma de de los numeros en una lista de numeros se usa la funcion sum()
#digitos_sum = []
#for digito in range(1, 11):
#	digitos_sum.append(digitos_sum)
#print(sum(digitos))

#*List comprehension
#Permite generar los anteriores programas en una sola linea 
#combiando el loop for y la creacion de nuevos elementos dntro 
#de una sola linea y automaticamente anexa cada nuevo elemento
#cuadrados = [valor**2 for valor in range (1, 11)]
#print(cuadrados)
