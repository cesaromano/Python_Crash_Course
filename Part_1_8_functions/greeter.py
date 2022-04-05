#	8.FUNCTIONS
#En este capitulo aprenderas a escribir funciones, las cuales son llamadas 
#bloques de codigo que son diseñadas para hacer un trabajo especifico.
#Cuando quieres realizar una tarea particular que has definido como una funcion
#llamas la funcion responsable por esto. Si necesitas realizar esa tarea multiples
#veces a lo largo de tu programa, no necesitas escribir todo el codigo para la 
#misma tarea una vez y otra; solo llama la funcion dedicada a manejar esa tarea
#y la llamada le dira a Python que corra el codigo dentro de la funcion. Encontraras
#que usar funciones hara tus programas masfaciles de escribir, leer, probar y
#reparar.
#En este capitulo tambien aprenderas formas de pasar informacion a funciones.
#Aprenderas como escribir ciertas funciones algunas de las cuales el trabajo
#principal es mostrar informacion y otras funciones diseñadas para procesar
#informacion y retornar un valor de un conjunto de valores. Finalmente,
#aprenderas a almacenar funciones en archivos separados llamados "modules" para
#ayudarte a rganizar tus archivos de programa principales.

#	DEFINIENDO UNA FUNCION

#def saludo_usuario():
#	"""Muestra un simple saludo."""
#	print("ACM1PT")

#saludo_usuario()

#La linea 1 usa la palabra clave "def"  para informarle a python que estas
#definiendo una funcion. Esta es la "function definition", que le dice a Python 
#el nombre de la funcion y si es aplicable, que tipo de informacion la funcion
#necesita para hacer este trabajo. El parentesis mantiene esta informacion. En este
#caso el nombre de la funcion es saludo_usuario(), y no necesita informacion para
#para hacer este trabajo, asi que el parentesis esta vacio. (Incluso asi, el
#parentesis es requerido) Finalmente, la definicion termina con dos puntos.
#Cualquier linea identada que siga def saludo_usuario(): hace parte del cuerpo de
#la funcion. El texto en la linea 2 es un comentario llamado "docstring", el cual
#describe lo que la funcion hace. Los Docstrings estan encapsulados en triples
#comillas, Las cuales busca Python cuando genera documentacion para las funciones
#en tus programas.
#La linea print("ACM1PT") es la unica linea de codigo real en el cuerpo de esta
#funcion, de tal modo que saludo_usuario() tiene solo un trabajo: print("ACM1PT").
#Cuando quieras usar esta funcion, la llamas. Un llamado de funcion le dice a 
#Python que ejecute el codigo en la funcion. Para llamar la funcion, escribes el
#nombre de la funcion, seguida por cualquier informacion necesaria en parentesis.

#*Pasando informacion a una funcion 
#Modificando ligeramente la funcion saludo_usuario() podra no solo decirle al usuario
#un saludo, si no que tambien podra incluir el nombre. Para que la funcion realice
#esto ingresa username en el parentesis de la definicion de la funcion. De esta
#manera le permitiras a la funcion que acepte cualquier valor de username que 
#especificaste. La funcion ahora espera que le proveas un valor a username cada vez
#que la llamas. Cuando llamas la funcion, puedes pasar un nombre dentro del parentesis

def saludo_usuario(usuario):
	"""Muestra un simple saludo"""
	print(f"ACM1PT, {usuario.title()}!")

saludo_usuario('santos')

#*Argumentos y parametros
#La variable usuario en la definicion de la funcion es un ejemplo de un parametro
#una pieza de informacion que la funcion necesita para hacer bien su trabajo. 
#El valor 'Santos' en la funcion es un ejemmplo de un argumento. Un argumento es
#una pieza de informacion que es pasada de una funcion llamada a una funcion.
#Cuando llamamos la funcion, colocamos el valor que queremos que la funcion trabaje
#en parentesis. En este caso el argumento 'Santos' ha pasado a la funcion y el 
#valor fue asignado al parametro usuario.