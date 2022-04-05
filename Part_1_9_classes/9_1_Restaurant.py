#Haz una clase llamada restaurante. el metodo __init__() debe almacenar dos atributos
#restaurant_name y cuisine_type. Crea un metodo llamado describe_restaurant()
#que imprima esas dos piezas de informacion, y un metodo llamado open_restaurant
#que imprima un mensaje que indique que el restaruante esta abierto.
#Haz una instancia llamando restaurant de tu clase. Imprime los dos atributos 
#individualmente y luego llama ambos metodos.

class Restaurant:
	"""Esta clase describe un restaurante"""

	def __init__(self, restaurant_name, cuisine_type):
		"""Inicializando atributos para describir el restaurante"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Describe el restaurante"""
		print(f"\n{self.restaurant_name}")
		print(f"{self.cuisine_type}")

	def open_restaurant(self):
		"""Describe si el restaurante esta abierto"""
		print(f"El restaurante {self.restaurant_name} de {self.cuisine_type}"
			" esta abierto.")

#restaurant_1 = Restaurant('Romano', 'Cocina criolla')
#restaurant_1.describe_restaurant()
#restaurant_1.open_restaurant()