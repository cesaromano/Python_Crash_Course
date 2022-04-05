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