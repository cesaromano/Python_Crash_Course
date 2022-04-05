#	USANDO UN LOOP WHILE CON LISTAS Y DICCIONARIOS
#Para mantener seguimiento de de muchos usuarios y piezas de informacion, 
#necesitaremos usar listas y diccionarios con nuestros loops while.
#Pra modificar una lista a medida que trabajas con ella, usa un loop while.
#Usando loops while con listas y diccionarios te permitira recolectar, almacenar,
#y organizar montones de input para examinar y reportar luego.

#*Moviendo items de una lista a otra
#Considera una lista de nuevos registros de usuarios sin verificar en un sitio web.
#Despues de verificar esos usuarios, como podemos moverlos a una lista separada
#de usuarios confirmados? Una forma puede ser usando un loop while para tomar
#los usuarios de la lista de usuarios sin confirmar asi los verificamos
#y luego los agregamos a una lista separada de usuarios confirmados:

#Comienza con usuarios que necesitan ser verificados, y una lista lista vacia
#para mantener los usuarios confirmados.

no_confirmados = ['alice', 'bryan', 'candance']
confirmados = []

#verifica cada usuario hasta que no halla mas usuarios no_confirmados.
#Mueve cada usuario verificado en la lista de usuarios verificados.

while no_confirmados:
	 usuario_actual = no_confirmados.pop()

	 print(f"Usuario verificado: {usuario_actual.title()}")
	 confirmados.append(usuario_actual)

#Mostrar todos los usuarios confirmados. 

print("\nLos siguientes usuarios han sido confirmados:")
for confirmado in confirmados:
	print(confirmado.title())

