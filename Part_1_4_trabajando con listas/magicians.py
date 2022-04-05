#4. WORKING WITH LISTS

#	LOOPING A LO LARGO DE UNA LISTA
# Para ealizar la misma accion para cada uno de los items en una lista se usa el loop "for"
#magicians = ['lorena', 'david', 'lina']
#for magician in magicians:
#	print(magician)

# *Una mirada mas cercana al looping
#El loop guarda cada valor de item en una variable temporal y repite la accion por cada item que contenga la lista
#el loop termina cuando ya no hay mas avalores en la lista 

#*Hciendo mas trabajo por medio del loop for 
#magicians = ['lorena', 'david', 'lina']
#for magician in magicians:
#	print(f"{magician.title()}, ese fue un gran truco hijo de perra!")
# identar se refiere a hacer un espacio a la derecha, se puede hacer con 
#la barra espaciadora o con la tecla tab
# se pueden escribir varias lineas identadas dentro del loop en seguida
#de la linea del loop y cada linea identada es ejecutada por cada item en la lista
#magicians = ['lorena', 'david', 'lina']
#for magician in magicians:
#	print(f"{magician.title()}, ese fue un gran truco hijo de perra!")
#	print(f"No puedo esperar para ver el proximo jodido acto de magia, {magician.title()}!")

#*Haciendo algo despues del loop for 
#Todas las lineas de codigo que no esten identadas despues del loop
#seran realizadas por una unica vez
#magicians = ['lorena', 'david', 'lina']
#for magician in magicians:
#	print(f"{magician.title()}, ese fue un gran truco hijo de perra!")
#	print(f"No puedo esperar para ver el proximo jodido acto de magia, {magician.title()}!\n")
#print("Muchas gracias por el acto sapos, ese fue un gran puto show!")

#	EVITANDO ERRORES DE IDENTACION
#Es comun cometer errores de identacion
#la identacion ayuda a tener un sentido general del codigo

#*Olvidando identar
#Siempre se debe identar la linea despues del loop, de no ser asi
#Python te lo recuerda
#magicians = ['lorena', 'david', 'lina']
#for magician in magicians:
#print(magician)
#Python espera encontrar una accion identada despues del loop, si no encuentra una
#te hara saber que linea tiene ese problema

#*Olvidando identar lineas adicionales
#por ejemplo
#magicians = ['lorena', 'david', 'lina']
#for magician in magicians:
#	print(f"{magician.title()}, ese fue un gran truco hijo de perra!")
#print(f"No puedo esperar para ver el proximo jodido acto de magia, {magician.title()}!\n")
#No reportara un error por que ya hay almenos una linea identada, 
#pero no incluira a la linea no identada dentro del loop, tomando el ultimo valor del codigo
#este es un error logico, la sintaxis es valida pero el codigo no produce el resultado
#deseado por que hay un error en esta logica 

#*Identando innecesariamente
#Ocurre cuando se identa una linea fuera de un loop. Python alertara acerca de un error de identacion
#message = "Hola putitos"
#	print(message)
#Solo se debe identar cuando cuando hay una razon especifica para ahcerlo, es decir 
#al momento solo dentro de un loop for

#*Identando innecesariamente despues de un loop
#Esto por lo general provoca un error de logica
#Es parecido al error de "*Olvidando identar lineas adicionales"
#pero de manera inversa

#Olvidando los dos puntos
#Los dos puntos al final de la linea de codigo de la declaracion for
#le dice a Python que interprete las siguientes lineas como el comienzo del loop
#esto produce un error de sintaxis. Aun que es un error facil de reparar
#no es un error facil de encontrar 
