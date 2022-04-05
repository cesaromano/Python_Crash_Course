#*Un diccionario de objetos similares
#Puedes tambien usar un diccionario para almacenar un tipo de informacion
#de varios objetos.
#Por ejemplo, quieres sondear un numero de personas y preguntarles cual es 
#es su lenguaje de programacion preferido. Un diccionario es util para 
#almacenar los resultados de una siemple encuesta:

#lenguajes_favoritos = {
#	'jen' : 'python',
#	'sarah' : 'c',
#	'edward' : 'ruby',
#	'phil' : 'python',
#}

#cada clave corresponde al nombre de la persona encuestada y cada valor es su
#eleccion.
#Para usar el diccionario, dando el nombre de una persona que realizo la encuesta
#puedes facilmente buscar tu lenguaje favorito:

#lenguaje = lenguajes_favoritos['sarah'].title()
#print(f"El lenguaje favorito de sarah es {lenguaje.title()}.")

#Puedes usar este mimo nombre de sitanxis con cualquier valor individual
#representado en el diccionario.

#hacer loop funciona particularmente bien para este ejemplo:

#for nombre, lenguaje in lenguajes_favoritos.items():
#	print(f"El lenguaje favorito de {nombre.title()} es {lenguaje.title()}.")

#*Looping a lo largo de las claves de un diccionario
#El metodo keys() es util cuando no necesitas trabajar con todos los valores del
#diccionario. Vamos a hacer loop a lo largo del diccionario lenguajes_favoritos
#e imprimir los nombres de cada uno que tomo la encuesta:

#for nombre in lenguajes_favoritos.keys():
#	print(nombre.title())

#Hacer loop a lo largo de las claves es es en realidad el comportamiento por 
#defecto cuando se hace un loop a lo largo de un diccionario, de esta manera
#este codigo obtendra la misma respuesta si se escribe:
#"for nombre in lenguajes_favoritos:"
#puedes usar el metodo keys() para hacer tu codigo mas legible.
#se puede acceder al valor asociado a cualquier clave que te interese dentro del
#diccionario usando la clave actual. Imprimamos un mensaje para una pareja de 
#amigos acerca del lenguaje que escogieron. Haremos loop a lo largo de los nombres
#en el diccionario como lo hicimos anteriormente, pero cuando coincida con el
#nombre de uno de nuestros amigos mostraremos el mensaje acerca de su lenguaje 
#favorito.

#amigos = ['phil', 'sarah']
#for nombre in lenguajes_favoritos.keys():
#	print(f"Hola {nombre.title()}.")

#	if nombre in amigos:
#		lenguaje = lenguajes_favoritos[nombre].title()
#		print(f"\t{nombre.title()}, Veo que te encanta {lenguaje}, perra!")

#Tambien puedes usar el metodo keys() para encontrar si una persona particular
#fue encuestada. Esta vez buscaremos si Erin realizo la encuesta:

#if 'erin' not in lenguajes_favoritos.keys():
#	print("Erin, colabora con la encuesta ome!")

#El metodo keys() no solo es para hacer loop: en realidad retorna una lista de 
#todas las llaves y simplemente verifica si 'erin' esta en la lista. 

#*Looping a lo largo de las llaves de un diccionario en un orden particular
#Aveces necesitaras hacer loop a lo largo de un diccionario en un orden diferente
#Una manera de hacer esto es ordenar las llaves como han sido retornadas 
#en el loop for, puedes usar la funcion sorted()para tener una copia 
#de las llaves en orden alfabetico:

#for nombre in sorted(lenguajes_favoritos.keys()):
#	print(f"{nombre.title()}, gracias por tomar la encuesta.")

#*Looping a lo largo de todos los valores en un diccionario
#Si estas interesado en los valores del diccionario puedes usar el metodo values()
#para retornar una lista de valores sin llaves.
#Por ejemplo, digamos que solamente queremos una lista de todos los lenguajes 
#escogidos en nuestra encuesta sin el nombre de la persona que selecciono cada
#lenguaje:

#print("Los siguientes lenguajes fueron mencionados:")
#for lenguaje in lenguajes_favoritos.values():
#	print(lenguaje.title())

#Este metodo puede trabajar bien con un numero pequeño de valores, pero en una
#encuesta con un largo numero de respondientes puede resultar en una lista muy 
#repetitiva. Para ver cada lenguaje escogido sin repeticion usamos set.
#Un set es una coleccion en la cual cada item llega a ser unico:

#for lenguaje in set(lenguajes_favoritos.values()):
#	print(lenguaje.title())

#Cuando envuelves ser al rededor de una lista que contiene items duplicados, 
#Python identifica los unicos items en la lista y construye un set de esos 
#items. 

#puedes construir un set directamente usando llaves y separando los elementos
#por comas:

#lenguajes = {'python', 'ruby', 'python', 'c'}
#print(lenguajes)

#Es un error comun confundir sets con diccionarios, para diferenciarlos,
#los diccionarios contienen pares de llaves-valores, mientras que los sets no.

#*Una lista en un diccionario
#Puedes anidar una lista dentro de un diccionario las veces que quieras mas de un
#valor para ser asociado con una simple llave en un diccionario. 
#para obtener los items asociados a esa llave se debe hacer un loop for por cada
#llave y dentro un loop for para cada valor:

lenguajes_favoritos = {
	'jen' : ['python', 'rubi'],
	'sarah' : ['c'],
	'edward' : ['ruby', 'go'],
	'phil' : ['python', 'haskell']
}

for nombre, lenguajes in lenguajes_favoritos.items():
	print(f"\nLos lenguajes favoritos de {nombre.title()} son:")
	for lenguaje in lenguajes:
		print(f"\t{lenguaje.title()}")