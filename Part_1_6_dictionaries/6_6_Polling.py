#Usa el codigo de lenguajes favoritos 

lenguajes_favoritos = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
}

#Realiza una lita de personas que deberia hacer la encuesta de lenguajes favoritos
#incluye algunos nombres que ya esten en el diccionario:

personas = ['romano', 'carlos', 'javier', 'nicoll', 'sarah', 'phil']

#Has un loop por la lista de personas, si ya han realizado la encuesta, imprime
#un mensje dandoles las gracias por responder. Si no han realizado la encuesta 
#escribe un mensaje invitandolos a realizarla:

for persona in personas:
	if persona in lenguajes_favoritos:
		print(f"{persona.title()}, gracias por responder hommie!")
	else:
		print(f"Responde esa monda {persona.title()}!")