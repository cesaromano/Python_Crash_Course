#7. USER IMPUT AND WHILE LOOPS
#Usualmente necitamos informacion del usuario. Por ejemplo, digamos que queremos
#saber si una persona tiene la suficiente edad para votar, si escribes un programa
#para resolver esta pregunta, necesitas conocer la edad del usuario antes de dar
#una respuesta. el programa necesitara solicitarle al usuario que ingrese o 
#input su edad, una vez que el programa tiene esaentrada puede comparar la edad
#de votacion para determinar si el usuario tiene la suficiente edad para votar.
#En este capitulo aprenderas como aceptar datos quue ingrese un usuario, para
#hacer esto usaras la funcion input().

#Tambien aprenderas como mantener los programas trabajando lo que el usuario 
#de manera que puedan ingresar toda la informacion que necesiten para que luego
#tu programa pueda trabajar con esa informacion. Usara el loop while de Pyhton 
#para mantener programas a medida que ciertas condiciones permanezcan verdaderas.

#	COMO FUNCIONA LA FUNCION INPUT()
#La funcion input() pausa el programa y espera hasta que el usuario entre algun 
#texto. Una vez que Python recibe el input, es asignado a una variable para
#hacer esa informacion conveniente para tu trabajo.
#Por ejemplo, el siguiente programa, le pide al usuario que ingrese algun texto
#luego muestra ese mensaje de vuelta al usuario:

#mensaje = input("Dime algo, y yo lo repetire:")
#print(mensaje)

#La funcion input() toma un argumento: la entrada, o instrucciones, que queremos 
#mostrar al usuario para que sepan que deben hacer. En este ejemplo, cuando 
#Python corre la primera linea el usuario ve la entrada "Dime algo, y yo lo repetire:"
#El programa espera mientras que el usuario ingresa su respuesta y continua despues
#de que el usuario presiona enter. 

#*Permitiendo al usuario elegir cuando salir
#Podemos hacer que el programa parrot.py corra todo lo que  el usuario quiera
#poniendo la mayoria del programa dentro de un loop while. Vamos a definir un
#valor de salida y luego mantener el programa corriendo tanto hasta que el 
#usuario no ingrese el valor de salida:

#prompt = "\nDime algo y lo repetire:"
#prompt += "\nIngresa 'salir' para finalizar el programa. "
#mensaje = ""
#while mensaje != 'salir':
#	mensaje = input(prompt)
#	print(mensaje)

#Para no imprimir el valor quit cuando se introduce se agrega un test if:

prompt = "\nDime algo y lo repetire:"
prompt += "\nIngresa 'salir' para finalizar el programa. "
#mensaje = ""
#while mensaje != 'salir':
#	mensaje = input(prompt)

#	if mensaje != 'salir':
#		print(mensaje)

#*Usando un "Flag"
#Que pasaria si muchos posibles eventos puedan ocurrir para parar el programa,
#intentar testar todas esas condiciones en una declaracion while se vuelve complicado
#y dificil.
#Para un programa que permita correr apenas ciertas condiciones que son verdaderas
#puedes definir una variable que determine si el programa entero esta activo.
#Esta variable, llamada "flag", actua como una señal para el programa. Podemos 
#escribir programas de manera que corran mientras que la bandera este en verdadero
#y pare de correr cuando alguno de varios eventos ajuste el valor de la bandera
#a falso. Como resultado toda la declaracion while necesita verificar solo una
#condicion: si el flag es actualmente verdadero. Despues, todos nuestros otros
#test pueden ser claramente organizados en el resto del programa.
#Vamos a agregar un flag al programa. Este flag, al cual vamos a llamar "activo",
#monitoreara si el programa debera seguir corriendo:

activo = True
while active:
	mensaje = input(prompt)

	if mensaje == 'salir':
		activo = False
	else:
		print(mensaje)

#Esto es util en programas complicados como juegos en los cuales puede haber 
#diferentes eventos que pueden hacer que el programa pare de correr. Cuando
#alguno de esos eventos causa que el flag activo se vuelva falso, el loop principal
#del juego saldra, un mensaje de game over puede ser mostrado, y se le puede
#dar al jugador la opcion de jugar de nuevo.

