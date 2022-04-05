#haz una lista de 5 o mas nombres de usuarios, incluyendo el nombre 'administrador'
#Imagina que estas escribiendo un codigo que saludara a cada usuario despues
#de haberse logueado en un sitio web. Haz un loop por la lista, e imprime un saludo
#a cada usuario:

usernames = ['admin', 'carlos', 'daniel', 'eduardo', 'santiago']

for username in usernames:
	if username == 'admin':
		print(f"Hola {username}, deseas el reporte motherfucker?")
	else:
		print(f"Hola {username}, Bienvenido madafaca!")

	