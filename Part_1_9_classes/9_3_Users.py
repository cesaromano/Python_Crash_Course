#Haz una clase llamada usuario. Crea dos atributos llamados fist_name y last_name
#

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

usuario_1 = User('Romano', 'Delgado', 24, 'Masculino')
usuario_1.describe_user()
usuario_1.greet_user()

usuario_2 = User('Rosalba', 'Marin', 54, 'Femenino')
usuario_2.describe_user()
usuario_2.greet_user()

usuario_3 = User('Victor', 'Garcia', 48, 'Masculino')
usuario_3.describe_user()
usuario_3.greet_user()