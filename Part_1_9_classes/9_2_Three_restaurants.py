#Inicia con la clase del ejercicio anterior. Crea tres instancias diferentes de
#la clase y llama describe_restaurant() de cada instancia

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

restaurant_1 = Restaurant('Romano', 'Cocina criolla')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('Victor', 'Cocina española')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('Rosalba', 'Cocina hindu')
restaurant_3.describe_restaurant()