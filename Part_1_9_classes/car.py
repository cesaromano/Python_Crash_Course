#	Working with Classes and Instances
#Una de las primeras tareas que querras hacer, es modificar los atributos 
#asociados con una instancia particular. Puedes modificar los atributos de una 
#instancia directamente o escribir metodos que actualicen atributos de formas
#especificas.

#*The Car Class
#Vamos a escribir una clase que represente un carro, almacenara informacion de
#un tipo de carro y tendra un metodo que sumarice esta informacion:

#class Car:
#	"""A attempt to represent a car"""

#	def __init__(self, make, model, year):
#		"""Initializate attributes to describe a car."""
#		self.make = make
#		self.model = model
#		self.year = year

#	def get_descriptive_name(self):
#		"""Return a neatly formatted descriptive name."""
#		long_name = f"{self.year} {self.make} {self.model}"
#		return long_name.title()

#my_new_car = Car('renault', 'sandero', '2013')
#print(my_new_car.get_descriptive_name())

#Setting a Default Value for an Attribute
#Pueden ser asignados valores por defecto sin pasar por atributos definiendolos
#en el mtodo __init__():

class Car:
	"""A attempt to represent a car"""

	def __init__(self, make, model, year):
		"""Initializate attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it")

#my_new_car = Car('renault', 'sandero', '2013')
#print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer()

#*Modifying Attribute Values
#Puedes cambiar el valor de un atributo en una instancia, en un metodo o
#incrementar su valor (agregar un cierto monto de el) en un metodo. 

#**Modifying an Attribute's Value Directly
#La forma mas simple de modificar el valor de un atributo es accesando al atributo
#desde una instancia:

#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()

#**Modifying an Attribute's Value Through a Method
#Puede ser de ayuda tener metodos que actualicen ciertos atributos por ti. En vez
#de accesar al atributo directamente, pasas el nuevo valor a un metodo que 
#maneje la actualizacion internamente:

#	def update_odometer(self, mileage):
#		"""Set the odometer reading to the given value"""
#		self.odometer_reading = mileage

#my_new_car = Car('renault', 'sandero', '2013')
#print(my_new_car.get_descriptive_name())
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()

#para evitar que alguien no intente volver atras el lector del odometro, se debe
#agregar una sentencia logica:

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

#my_new_car = Car('renault', 'sandero', '2013')
#print(my_new_car.get_descriptive_name())
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()
#my_new_car.update_odometer(24)
#my_new_car.read_odometer()

#**Incrementing an Attribute's Value Through a Method
#Digamos que compramos un auto usado y ponemos 100 millas en el entre el tiempo
#que lo compramos y el tiempo que lo registramos:

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

my_used_car = Car('renault', 'sandero', '2013')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()