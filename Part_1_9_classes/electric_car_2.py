#*Importing a Module into a Module
#Aveces querras desplgar tus classes en varios modulos para mantener 
#cualquier file de crecimiento muy largo y evitando almacenar clases 
#sin relacion en el mismo modulo. Cuando almacenas tus clases en varios
#modulos, encontraras que una class en un module depende de una clase en 
#otro modulo. Cuando esto pasa, puedes importar la clase requerida en
#el primer module.

from car import Car

class Battery:
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size = 75):
		"""Initialize the battery's attributes"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initialize atributes of the parent class.
		Then initialize attributes specific to an electric car
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

#La clase ElectricCar necesita acceso de su parent class Car, asi que
#importamos Cardirectamente en el modulo. Si olvidamos esa linea, 
#Python dara un error. Tambien necesitaremos actualizar el modulo Car
#de manera que solo contenga la class Car.

#*Usando Alias
#los alias son pueden ser de ayuda cuando usamos modulos para
#organizar proyectos de codigo. Puedes usar alias cuando importes
#clases tambien, se usa la sintaxis:

#from electric_car import ElectricCar as EC

#Ahora puedes usar este alias cada vez que quieras hacer un carro 
#electrico:
#my_tesla = EC('tesla', 'roadster', 2019)

#*Encontrando tu propio flujo de trabajo
#Python ofrece varias opciones para estructurar codigo en un proyecto
#largo. Es importante conocer todas esas posibilidades para determinar
#las mejores maneras para organizar tus proyectos tambien para entender
#los proyectos de otros.

#Cuando comiences, manten tu estructura de codigo simple. Intenta
#hacer todo en un archivo y moviendo tus clases a modulos separados
#una vez que todo este funcionando. Si te gusta como los modulos 
#y archivos interactuan, intenta almacenar tus clases en modulos 
#cuando inicias un proyecto. 