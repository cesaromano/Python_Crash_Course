#agrega un atributo llamado number_served con un valor por defecto de 0, crea 
#una estancia llamada restaurant de esta clase. Imprime el numero de usuarios
#al que el restaurante ha servido, luego cambia este valor e imprimelo de nuevo

class Restaurant:
	"""Esta clase describe un restaurante"""

	def __init__(self, restaurant_name, cuisine_type):
		"""Inicializando atributos para describir el restaurante"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Describe el restaurante"""
		print(f"\n{self.restaurant_name}")
		print(f"{self.cuisine_type}")

	def open_restaurant(self):
		"""Describe si el restaurante esta abierto"""
		print(f"El restaurante {self.restaurant_name} de {self.cuisine_type}"
			" esta abierto.")

	def read_customer_served(self):
		print(f"Se ha servido a {self.number_served} clientes")

	def set_number_served(self, served):
		"""Permite ajustar el numero de usuarios que han sido servidos"""
		self.number_served = served
		

	def increment_number_served(self, increment):
		"""Aumenta el numero de usuarios servidos"""
		self.number_served += increment

restaurant_1 = Restaurant('Romano', 'Cocina criolla')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_1.set_number_served(15)
restaurant_1.read_customer_served()
restaurant_1.set_number_served(16)
restaurant_1.read_customer_served()
restaurant_1.increment_number_served(15)
restaurant_1.read_customer_served()

