#Tomar los ejemplos del ejercicio foods.py
mis_comidas = ['carne', 'burritos', 'lassagna', 'torta de maiz']
amigo_comidas = mis_comidas [:]

mis_comidas.append('chorizo')
amigo_comidas.append('arepa')

print("Mis comidas favoritas son:")
for comida in mis_comidas:
	print(f"\n{comida.title()}")

print("\n Las comidas favoritas de mi amigo son:")
for amigo_comida in amigo_comidas:
	print(f"\n{amigo_comida.title()}")