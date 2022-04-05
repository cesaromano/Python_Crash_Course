#Considremos un programa que determine si las personas son suficientemente altas
#para montar en una montaña rusa:

estatura = input("Cual es tu estatura en cm? ")
estatura = int(estatura)

if estatura >= 121:
	print("\nTienes la estatura suficiente para montar")
else:
	print("\nPodras montar cuando seas un poco mas grande hijito")

#Cuando usas input numerico, asegurate de convertir el valor a una representacion
#numerica antes.

#*El operador MODULO
#Una herramienta util para trabajar con informacion numerica es el operador modulo
#(%), que divide un numero por otro y entrega el residuo:

#>>> 5 % 3
#2
#>>> 6 % 3
#0
#>>> 7 % 3
#1 