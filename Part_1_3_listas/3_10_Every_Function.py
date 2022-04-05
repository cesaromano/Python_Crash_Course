#Crea una lista de lo que quieras
novias = ['nicoll', 'alejandra', 'lorena', 'angy']
#Funcion imprimir todos los items
print(novias)
#Funcion imprimir por posicion 0
print(novias[0])
#Funcion imprimir por posicion diferente de 0
print(novias[1])
#Funcion metodo title() a cada elemento de la lista
print(novias[0].title())
#Funcion imprimir ultimo Item con -1
print(novias[-1])
#Funcion usar items como valores
message = (f"la pase una chimba con {novias[2].title()}")
print(message)
#Funcion cambiar el valor de un item en la lista
novias[3] = 'laura'
print(novias)
#Funcion anexar item al final de la lista con metodo append()
novias.append('angelica')
print(novias)
#Funcion insertar item en alguna posicion de la lista con el metodo insert()
novias.insert(1, 'carolina')
print(novias)
#Funcion eliminar elemento de la lista usando la declaracion del
del novias[1]
print(novias)
#Funcion remover ultimo item de la lista usando el metodo pop()
novias.pop()
print(novias)
#Funcion utilizar item removido con metodo pop()
novia_removida = novias.pop()
print(novia_removida)
#Funcion utilizar item removido como variable con metodo pop()
message_2 = (f"Habria sido interesante tener algo con {novia_removida.title()}")
print(message_2)
#Funcion utilizar item removido como variable de acuerdo a posicion con metodo pop()
ultima_novia = novias.pop(0)
message_3 = (f"Actualemente vivo muy feliz al lado de {ultima_novia.title()}")
print(message_3)
#Funcion removiendo un valor por su valor con el metodo remove()
novias.remove('alejandra')
print(novias)
#Funcion removiendo un valor y utilizandolo en una variable con el metodo remove()
no_novia = 'lorena'
novias.remove(no_novia)
print(novias)
message_4 = (f"{no_novia.title()} no fue una novia para mi en realidad")
print(message_4)
#Funcion ordenar items alfabeticamente con el metodo sort()
novias = ['nicoll', 'alejandra', 'lorena', 'angy']
novias.sort()
print(novias)
#Funcion ordenar items alfabeticamente de manera inversa con el argumento reverse=True
novias.sort(reverse=True)
print(novias)
#Funcion ordenar items alfabeticamente sin alterar orden original con la funcion sorted()
print(sorted(novias))
#Funcion ordenar items de manera inversa con el metodo reverse()
novias.reverse()
print(novias)
#Funcion determinando la longitud de items de una lista con la funcion len()
print(len(novias))