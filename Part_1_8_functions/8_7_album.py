#escribe una funcion llamada hacer_album() que construya un diccionario descri
#biendo un album musical. la funcion debera tomar el nombre de un artista y un
#titulo de album y debera retornar un diccionario conteniendo esas dos piezas
#de informacion. Usa la funcion para hacer tres diccionarios representando 
#diferentes albumes. Imprime cada valor retornado para mostrar que los diccionarios
#estan almacenando la informacion del album correctamente.
#Usa none para agregar un parametro opcional para la funcion que te permita
#almacenar el numero d canciones de un album. Si la linea de llamada incluye un
#valor para el numero de canciones, agrega el valor al diccionario del album. 
#Realiza al menos una nueva llamada de funcion que incluya el numero de canciones
#en un album.

def crear_album(artista, album, numero_canciones= None):
	if numero_canciones:
		nuevo_album = {'artista': artista, 'album': album,
		'numero de canciones': numero_canciones}
		return nuevo_album
	else:
		nuevo_album = {'artista': artista, 'album': album}
		return nuevo_album

album_p = crear_album('victor', 'niño viajero')
print(f"\n{album_p}")

album_p = crear_album('santos', 'ese tipo cool')
print(f"\n{album_p}")

album_p = crear_album('lucas', 'la madre')
print(f"\n{album_p}")

album_p = crear_album('mario', 'mario el bohemio', 12)
print(f"\n{album_p}")