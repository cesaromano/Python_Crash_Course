#*LLenando un diccionario con input del usuario 
#Puedes solicitar toda la informacion que necesites en cada paso a lo largo del 
#loop while. Hagamos un programa de encuestas en el cual cada paso porel loop
#solicite a los participantes nombre y respuesta. Almacenaremos la informacion
#que obtengamos en un diccionario, por que queremos conectar cada respuesta con
#un usuario particula:

respuestas = {}

#Configuremos una bandera para indicar que la encuesta esta activa.

encuesta_activa = True

while encuesta_activa:
	#Solicitemos el nombre de la persona y su respuesta.
	nombre = input("\nCual es tu nombre? ")
	respuesta = input("\nQue montaña te gustaria escalar algun dia? ")

	#Almacenar la respuesta en el diccionario
	respuestas[nombre] = respuesta

	#Buscando si alguien mas va a tomar la encuesta
	repetir = input("Quieres permitir que alguien mas responda? (si/no) ")
	if repetir == 'no':
		encuesta_activa = False 

#La respuesta esta completa. Mostrando los resultados.
print("\n---Resultados de la encuesta---")
for nombre, respuesta in respuestas.items():
	print(f"A {nombre.title()} le gustaria escalar la montaña {respuesta}")