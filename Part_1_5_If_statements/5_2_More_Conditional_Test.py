#Ten al menos un resultado falso y uno verdadero para cada uno de los siguientes
#casos:

#Test para igualdades y desiguladades en strings

#pizza =  'mexicana'
#print(f"Es pizza != 'mexicana'? Predigo que es falso.")
#print(pizza != 'mexicana') 

#print("\n Es pizza == 'hawaiana'? Predigo que es verdadero.")
#print(pizza != 'hawaiana')

#Test usando el metodo lower()

#persona = 'Andrea'
#print(f"Es persona == 'andrea'? Predigo que es verdadero.")
#print(persona.lower() == 'andrea') 

#print("\n Es persona == 'Andrea'? Predigo que es falso.")
#print(persona.lower() == 'Andrea')

#Test numerico involucrando comparaciones matematicas

#print(f"Es 1 == 2? Predigo que es falso.")
#print(1 == 2) 

#print("\n Es 1 == 1? Predigo que es verdadero.")
#print(1 == 1)

#print(f"Es 1 != 2? Predigo que es verdadero.")
#print(1 != 2) 

#print("\n Es 1 != 1? Predigo que es falso.")
#print(1 != 1)

#print(f"Es 1 > 2? Predigo que es falso.")
#print(1 > 2) 

#print("\n Es 1 > 1? Predigo que es falso.")
#print(1 > 1)

#print(f"Es 1 > 2? Predigo que es falso.")
#print(1 >= 2) 

#print("\n Es 1 > 1? Predigo que es verdadero.")
#print(1 >= 1)

#print(f"Es 1 < 2? Predigo que es verdadero.")
#print(1 < 2) 

#print("\n Es 1 < 1? Predigo que es falso.")
#print(1 < 1)

#print(f"Es 1 <= 2? Predigo que es verdadero.")
#print(1 <= 2) 

#print("\n Es 1 <= 1? Predigo que es verdadero.")
#print(1 <= 1)

#Test usando las palabras and y or

#num_1 = 5

#print(f"Es num_1 < 2 y num_1 > 10? Predigo que es falso.")
#print(num_1 < 2 and num_1 > 10) 

#print("\n Es num_1 > 2 and num_1 < 10 Predigo que es verdadero.")
#print(num_1 > 2 and num_1 < 10)


#num_1 = 5

#print(f"Es num_1 < 2 or num_1 > 10? Predigo que es verdadero.")
#print(num_1 > 2 or num_1 > 10) 

#print("\n Es num_1 > 2 or num_1 < 10 Predigo que es verdadero.")
#print(num_1 > 2 or num_1 < 10)

#Test si un item esta en la lista 

#aderezos_requeridos = ['champiñones', 'cebolla', 'piña']
#print("Esta champiñones dentro de los aderezos?")
#print('champiñones' in aderezos_requeridos) 

#print("Esta papas dentro de los aderezos?")
#print('papas' in aderezos_requeridos)

#Test si un item no esta en la lista

aderezos_requeridos = ['champiñones', 'cebolla', 'piña']
print("champiñones esta en aderezos requeridos?")
if 'champiñones' not in aderezos_requeridos:
	print("No esta!")
else:
	print("Si esta!")

print("\n papas esta en aderezos requeridos?")
if 'papas' not in aderezos_requeridos:
	print("No esta!")
else:
	print("Si esta!")




