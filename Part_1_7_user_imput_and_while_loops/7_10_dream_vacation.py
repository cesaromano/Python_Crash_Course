#Escribe un programa que encueste a los usuarios acerca de las vaciones de sus
#sueños. Incluye un bloque de codigo que imprima el resultado de la encuesta:

respuestas = {}

encuesta_activa = True

while encuesta_activa:
	nombre = input(f"Cual es tu nombre? ")
	respuesta = input(f"Si fueras a un lugar de vacaciones, cual seria? ")

	respuestas[nombre] = respuesta

	repetir = input("\nDeseas encuestar mas personas? (si/no) ")
	if repetir == 'no':
		encuesta_activa = False

print("\n---Resultados de la encuesta---")
for nombre, respuesta in respuestas.items():
	print(f"{nombre.title()} dijo que le gustaria ir de vacaciones a {respuesta}")
