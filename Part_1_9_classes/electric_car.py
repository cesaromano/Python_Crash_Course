#	INHERITANCE
#Puedes usar Inheritance para escribir una version especializada de
#otra clase que has escrito, cuando una clase hereda de otra, toma
#los atributos y metodos de la primera clase. La clase original es
#llamada parent class y la nueva clase es llamada child class. La
#nueva clase hereda todos os atributos de la parent class pero es libre
#de definir nuevos atributos y metodos.

#*The __init__() Method for a Child Class
#Para inicializar los atributos de la parent class se llaman el metodo
#__init__() y hacerlos disponibles en la child class.
#Como ejemplo vamos a modelar un carro electrico:

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

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

#class ElectricCar(Car):
#	"""Represent aspects of a car, specific to electric vehicles."""

#	def __init__(self, make, model, year):
#		"""Initialize atributes of the parent class."""
#		super().__init__(make, model, year)

#my_tesla = ElectricCar('tesla', 'model s', 2019)
#print(my_tesla.get_descriptive_name())

#la funcion especial super(), viene de la convencion de llamar the
#parent class como superclass y the child class como subclass.
#La instancia ElectricCar trabaja como una instancia de Car, asi que 
#ahora podemos comenzar a definir los atributos y metodos necesarios
#para diferenciar the child class.

#*Defining attributes and Methods for the Child Class
#Puedes agregar nuevos atributos y metodos necesarios para diferenciar
#la child class de la parent class.

#		"""Initialize attributes of the parent class.
#		Then initialize attributes specific to an electric car.
#		"""

#		self.battery_size = 75

#	def describe_battery(self):
#		"""Print a statement describing the battery size."""
#		print(f"This car has a {self.battery_size} - kWh battery.")

#my_tesla = ElectricCar('tesla', 'model s', 2019)
#print(my_tesla.get_descriptive_name())
#my_tesla.describe_battery()

#*Overriding Methods from the Parent Class
#Puedes anular cualquier metodo de la parent class que no se ajuste a
#lo que estas tratando de modelar con la child class. Para hacerlo
#defines un metodo en la child class con el mismo nombre del metodo
#que quieres anular en la parent class. Python ignorara el metodo de la
#parent class y solo pondra atencion al metodo que definas en la child
#class:

#	def fill_gas_tank(self):
#		"""Electric cars don't have gas tanks."""
#		print("This car doesn't ned a gas tank")

#Si alguien intenta llamar el metodo fill_gas_tank() con un carro
#electrico, Python ignorara el metodo en Car y correra este codigo 

#*Instances as Attributes
#Situaciones en las que tus archivos se vuelvan extensos, podras
#reconocer que parte de una clase puede ser escrita como una clase
#separada. Puedes partir tu clase larga en pequeñas clases que 
#trabajen juntas.
#Por ejemplo, si continuamos añadiendo detalles la ElectricCar clas,
#nos daremos cuenta de que estamos añadiendo atributos y metodos 
#especificos de la bateria. Podemos mover esos metodos y atributos a
#una clase separada llamada battery. Luego podemos usar una instancia
#de battery como un atributo en ElectricCar class:

class Battery:
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size = 75):
		"""Initialize the battery's attributes"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

#class ElectricCar(Car):
#	"""Represent aspects of a car, specific to electric vehicles."""

#	def __init__(self, make, model, year):
#		"""
#		Initialize atributes of the parent class.
#		Then initialize attributes specific to an electric car
#		"""
#		super().__init__(make, model, year)
#		self.battery = Battery()

#my_tesla = ElectricCar('tesla', 'model s', '2019')

#print(my_tesla.get_descriptive_name())
#my_tesla.battery.describe_battery()

#Esto parece mucho trabajo, pero ahora podemos describir la bateria
#mas detalladamente que si no se cortara la clase ElectricCar.
#Agreguemos otro metodo a Battery que reporte el rango del carro basado
#en el tamaño de la bateria:

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

my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#*Modeling Real-World Objects
#