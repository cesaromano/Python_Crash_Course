# los parentesis cuadrados ([]) indican listas, y sus elementos individuales se separan por comas 
bicycles = ['treek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# para accesar al elemento de una lista se describe el nombre de la lista seguido por el numero de 
# posicion del elemento entre parentesis cuadrados
print(bicycles[0])
# se pueden usar los metodos de formato "string" del capitulo 2
print(bicycles[0].title())
# para accesar al elemento 2, se busca por su inidce "1"
print(bicycles[1])
# para accesar al elemento 2, se busca por su inidce "1"
print(bicycles[3])
# para accesar al utimo elemento se usa el indice "-1"
print(bicycles[-1])
# se puede usar el valor dentro de una lista como se usa cualqueir variable
# dentro de un string
message = f'No tengo ni puta idea de lo que significa "{bicycles[0].title()}"'
print(message)