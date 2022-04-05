#imprime una lista de un millon de digitos 
#metodo largo (el tercero mas rapido 1.5s)
#un_millon = []
#for valor in range (1, 1000001):
#	un_millon.append(valor)
#print(un_millon)
#metodo list comprehension (el segundo mas rapido 1.3s)
#un_millon = [valor*1 for valor in range (1, 1000001)]
#print(un_millon)
#metodo con funcion lista (el mas rapido 1.1s)
un_millon = list(range(1, 1000001))
print(un_millon)