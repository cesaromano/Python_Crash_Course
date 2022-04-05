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

class IceCreamStand(Restaurant):
	"""Representa aspectos de una heladeria"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Inicializa atributos de la parent class"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['vainilla', 'ron con pasas', 'frutos rojos']

	def display_flavors(self):
		"""Muestra los sabores"""
		print(f"Los sabores son: {self.flavors}")

ice_cream_restaurant = IceCreamStand('Romano', 'Heladeria')
ice_cream_restaurant.describe_restaurant()
ice_cream_restaurant.display_flavors()