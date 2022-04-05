class User:
	"""Esta clase representa un usuario"""

	def __init__(self, first_name, last_name, age, sex):
		self.first_name = first_name
		self.last_name =last_name
		self.age = age
		self.sex = sex
		self.login_attempts = 0

	def describe_user(self):
		"""Describe el usuario"""
		print(f"\nNombre: {self.first_name}")
		print(f"Apellido: {self.last_name}")
		print(f"Edad: {self.age}")
		print(f"Sexo: {self.sex}")

	def greet_user(self):
		"""Saluda el usuario"""
		print(f"Hola {self.first_name}. Bienvenido!")

	def read_attempts(self):
		"""Describe el numero de intentos"""
		print(f"Numero de intentos {self.login_attempts}")

	def increment_login_attempts(self):
		"""Incrementa el valor de numero de intentos a 1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Resetea el numero de intentos del login"""
		self.login_attempts = 0

usuario_1 = User('Romano', 'Delgado', 24, 'Masculino')
usuario_1.describe_user()
usuario_1.greet_user()
usuario_1.read_attempts()
usuario_1.increment_login_attempts()
usuario_1.read_attempts()
usuario_1.increment_login_attempts()
usuario_1.read_attempts()
usuario_1.increment_login_attempts()
usuario_1.read_attempts()
usuario_1.reset_login_attempts()
usuario_1.read_attempts()