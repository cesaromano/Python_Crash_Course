from user_module import User

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