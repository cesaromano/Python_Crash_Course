#*Verificando si un valor no esta en una lista
#Otras veces es importante verificar si un valor no apparece en tu lista.
#puedes usar la palabra not en esta situacion.

banned_users = ['carlos', 'daniel', 'david']
user = 'romano'

if user not in banned_users:
	print(f'{user.title()}, puedes postear una respuesta si lo deseas.')

# *Boolean expressions
#Expresion booleana no es mas que otro nombre para test condicional
#un valor booleano es o verdadero o falso.
#Los valores booleanos son usados amenudo para dejar ciertas condiciones, tales 
#como si un juego esta corriendo o si un usuario puede editar cierto contenido 
#en un sitio web:

#game_active = True
#can_edit = false

#Los valores booleanos proveen una manera eficiente de seguir el estado de un
#programa o una condicion particular que es importante en tu programa.

