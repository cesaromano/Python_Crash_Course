#Haz una copia de la lista de pizzas del ejercicio 4_1 y llamala pizzas_amigo
pizzas = ['mexicana', 'ranchera', 'margarita', 'calabresa']
pizzas_amigo = pizzas [:]
#Agrega una nueva pizza a la lista original
pizzas.append('hawaiana')
#Agrega una pizz diferente a la lista de pizzas de tu amigo
pizzas_amigo.append('chocolate')
#prueba imprimiendo mensajes en un loop for de cada una de las pizzas tuyas y de
#tu amigo
print("Mis pizzas favoritas son:")
for pizza in pizzas:
	print(f"\n {pizza.title()}")
print("\nLas pizzas favoritas de mi amigo son:")
for pizza_amigo in pizzas_amigo:
	print(f"\n {pizza_amigo.title()}")