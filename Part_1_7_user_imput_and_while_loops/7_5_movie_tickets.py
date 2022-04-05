#Un cinema carga diferentes precios de tickete dependiendo de la edad de la 
#persona. Si la persona esta por debajo de 3 años, el ticket es gratis, si esta
#entre 3 y 12 años, el ticket es a 30.000, y si es mayor de 15 años el ticket es
#a 45.000. Escribe un loop en el cual le pidas al usuario su edad y luego dile el
#costo del ticket.

prompt = "\nIngresa tu edad para saber la tarifa de la entrada:"
prompt += "\nSi ya terminaste escribe 'salir'" 

while True:
	edad = input(prompt)

	if edad == 'salir':
		break
	else:
		edad = int(edad)

		if edad <= 3:
			print(f"\nLa entrada es gratuita")
		elif edad <= 12:
			print(f"\nEl valor de la entrada es de 30.000")
		elif edad > 12:
			print(f"\nEl valor de la entrada es de 45.000")




