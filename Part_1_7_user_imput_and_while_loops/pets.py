#*Removiendo todas las instancias d valores especificos de una lista
#Que pasa siq uieres remover todas las instancias de un valor valor de una lista?
#Digamos que tienes una lista de mascotas con el valor 'cat' repetido varias 
#veces. Para remover todas las instancias de ese valor, puedes correr un loop while
#hasta que 'cat' ya no este mas en la lista:

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)