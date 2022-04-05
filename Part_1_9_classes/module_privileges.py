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

class Privileges:
	"""Describe los privilegios del usuario"""
	def __init__(self):
		self.privileges = ['agregar posts', 'eliminar posts',
		'bannear posts']

	def show_privileges(self):
		"""Muestra los privilegios del usuario"""
		print(f"El usuario cuenta con los siguientes privilegios: ")
		for privilege in self.privileges:
			print(privilege)

class Admin(User):
	"""Describe el tipo de usuario Administrador"""
	def __init__(self, first_name, last_name, age, sex):
		"""Inicializa atributos de la parent class"""
		super().__init__(first_name, last_name, age, sex)
		self.privilegess = Privileges()