#inicia con el programa del ejercicio anterior. Escribe un loop while que te
#permita al usuario ingresar el un artista y titulo de album.  Una vez que tengas
#esa informacion, llama la funcion con el input del usuario e imprime el 
#diccionario que fue creado, asegurate de incluir un valor de salida en el loop
#while

def crear_album(artista, album):

	nuevo_album = {'artista': artista, 'album': album}
	nuevo_album['artista'] = artista
	nuevo_album['album'] = album

	return nuevo_album

while True:

	print("\nDanos algunos datos sobre tu musica: ")
	print("Si no quieres seguir guardando albumes pulsa 'q' ")

	artista = input("Ingresa el nombre de tu artista: ")
	if artista == 'q':
		break

	album = input("Ingresa el titulo del album: ")
	if album == 'q':
		break

	album_creado = crear_album(artista, album)
	print(album_creado)