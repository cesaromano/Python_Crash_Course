#*Usando break para salir de un loop
#Para salir de un loop while inmediatamente sin correr algun restante de codigo
#en el loop, independiente de los resultados de cualquier test condicional, usa la
#declaracion "break". La declaracion break dirije el flujo de tu programa, puedes
#usarlo para controlar cuales lineas de codigo son ejecutadas y cuales no, de manera
#que el programa solo ejecuta el codigo que quieres, cuando tu quieres.
#Por ejemplo, considera un programa que le pregunte al usuario acerca de lugares
#que han visitado. Podemos parar el el loop while en este programa llamando a
#break tan pronto el usuario ingrese el valor 'quit':

prompt = "\nIngresa el nombre de las ciudades que has visitado:"
prompt += "\n(Ingresa 'salir' cuando hallas finalizado)"

while True:
	city = input(prompt)

	if city == 'salir':
		break
	else:
		print(f"\nDebe ser genial conocer {city.title()}!")

#La declaracion break se puede usar en cualquier loop.
