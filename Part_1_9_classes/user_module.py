class User:
	"""Esta clase representa un usuario"""

	def __init__(self, first_name, last_name, age, sex):
		self.first_name = first_name
		self.last_name =last_name
		self.age = age
		self.sex = sex

	def describe_user(self):
		"""Describe el usuario"""
		print(f"\nNombre: {self.first_name}")
		print(f"Apellido: {self.last_name}")
		print(f"Edad: {self.age}")
		print(f"Sexo: {self.sex}")

	def greet_user(self):
		"""Saluda el usuario"""
		print(f"Hola {self.first_name}. Bienvenido!")