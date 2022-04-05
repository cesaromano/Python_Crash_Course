#Has una lista llamada sandwich_ordenes y llenala con los nombres de varios
#sandwiches. 

ordenes_empanadas = ['carne', 'pollo', 'mixta', 'queso', 'vegetariana']

#Luego has una lista vacia llamada empanadas_finalizadas. loop por la lista de 
#ordenes_empanadas e imprime un mensaje para cada orden, cada vez que cada empanada
#este terminada, muevela a la lista de empanadas finalizadas. Despues de que todas
#las empanadas esten terminadas, imprime un mensaje listando cada empanada que fue
#hecha:

empanadas_finalizadas = []

while ordenes_empanadas:
	empanada_actual = ordenes_empanadas.pop()
	print(f"\nOrdenando empanada {empanada_actual.title()}")
	empanadas_finalizadas.append(empanada_actual)

print("\nFueron realizadas las siguientes empanadas:")
for empanada in empanadas_finalizadas:
	print(empanada.title())