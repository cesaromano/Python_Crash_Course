#Creamos un archivo separado que importara la class Car y creara una
#instancia desde ella

from car_2 import Car

my_new_car = Car('renault', 'sandero', 2013)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Importar classes es una forma efectiva de programar. Cuando mueves
#la class a un module e importas el module, obtienes la misma
#funcionalidad, pero mantienes tu programa principal limpio y facil
#de leer. Tambien almacenas la mayoria de la logica en files separados
#una vez que tus classes trabajen como quieres que trabajen, puedes
#dejar esos files solos y enfocarte en el nivel superior de tu programa
#principal.

