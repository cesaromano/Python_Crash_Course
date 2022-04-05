#Usando la lista de las empanadas del ejercicio anterior, asegurate que la
#empanada de pastrami aparesca en la lista al menos 3 veces. Agrega codigo al
#principio de tu programa para imprimir un mensajeque diga "nos quedamos sin 
#pastrami" y luego usa un loop while para remover todas las instancias de 'pastrami'
#de ordenes_empanadas. Asegurate que no hallan ordenes finalizadas de empanadas
#de pastrami:

ordenes_empanadas = ['carne', 'pastrami','pollo', 'pastrami', 'mixta', 'queso', 
'vegetariana', 'pastrami']

empanadas_finalizadas = []

print(f"Nos quedamos sin pastrami")

while 'pastrami' in ordenes_empanadas:
	ordenes_empanadas.remove('pastrami')

while ordenes_empanadas:
	empanada_actual = ordenes_empanadas.pop()
	print(f"\nOrdenando empanada {empanada_actual.title()}")
	empanadas_finalizadas.append(empanada_actual)

print("\nFueron realizadas las siguientes empanadas:")
for empanada in empanadas_finalizadas:
	print(empanada.title())