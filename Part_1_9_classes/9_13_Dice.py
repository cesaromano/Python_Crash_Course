class Die:
	"""Modela un dado de varios lados"""

	def __init__(self, sides = 6):
		"""Inicializa los atributos"""
		self.sides = sides

	def roll_die(self):
		"""
		Imprime un numero entre 1 y el numero de ladosque el dado
		tenga
		"""
		from random import randint
		num = randint(1, self.sides)
		print(num)

six_die = Die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()
six_die.roll_die()

ten_die = Die(10)
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()
ten_die.roll_die()

twenty_die = Die(20)
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()
twenty_die.roll_die()