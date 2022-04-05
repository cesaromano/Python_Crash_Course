#*Importing Multiple  Classes from a Module
#Puedes importar cuantas classes necesites en un program file:

#from car_3 import Car, ElectricCar

#my_beetle = Car('volkswagen', 'beetle', 2019)
#print(my_beetle.get_descriptive_name())

#my_tesla = ElectricCar('tesla', 'roadster', 2019)
#print(my_tesla.get_descriptive_name())

#Importas multiples classes de un modulo separando cada class con una
#coma

#*Importing an Entire Module
#Puedes importar un modulo entero y luego accesar a las classes que
#necesites usando la notacion de punto. Esta forma es facil de leer
#por que cada llamada que cree una instancia de una class incluye el
#nombre del modulo, no tendras conflictos de nombrado con ninguno
#de los nombres usados en el file actual:

import car_3

my_beetle = car_3.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car_3.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

#*Importing All Classes from a Module
#Puedes importar cada class de un modulo usando la siguiente syntaxis
#from module_name import*
#Este metodo no es recomendado por dos razones. Primero, es de ayuda
#poder leer los statements import en la parte alta de un file y tener
#claro cuales classes usa un programa. De esta manera no es claro cuales
#clases estas usando desde el modulo. Este modo puede tambien generar
#confusion con nombres en el archivo. Si accidentalmente importas una
#class con el mismo nombre de algo mas en tu file, puedes crear errores
#que seran dificiles de diagnosticar. 
#Si necesitas importar muchas classes desde un module, sera mejor importar
#el modulo entero y usar la syntaxis module_name.ClassName. Evitando
#los conflictos potenciales de nombrado.