#Has un diccionario llamado, lugares favoritos
#Piensa en tres nombres para usar como llaves en el diccionario, y almacena
#de uno a tres lugares favoritos de cada persona: 

lugares_favoritos = {
	'romano': ['casa', 'exterior', 'agua'],
	'victor': ['casa abuelos', 'parque florida', 'casa'],
	'rosalba': ['casa', 'parque simon bolivar', 'casa graciela'],
	'sergio' : ['villavicencio', 'casa', 'videojuegos'],
}

#Has un loop a lo largo del diccionario e imprime cada nombre de la persona y sus
#lugares favoritos:

for persona, lugares in lugares_favoritos.items():
	print(f"\nLos lugares favoritos de {persona.title()} son:")
	for lugar in lugares:
		print(f"\t{lugar.title()}")
