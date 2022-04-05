#*Usando get() para accesar valores
#Usar llaves en parentesis cuadrados para obtener el valor en el que estas
#interesado de un diccionario puede causar un problema potencial: si la llave
#por la que tu preguntas no existe, tendras un error.
#Vamos a ver que pasa cuando preguntas por el valor de la puntuacion de un alien
#que no tiene un conjunto de valores en su puntuacion:

alien_0 ={
	'color' : 'verde',
	'valocidad' : 'lenta',
}

#print(alien_0['puntos'])
#Para diccionarios se usa el metodo get() para establecer un valor determinado
#que sera retornado si la calve requerida no existe.
#El metodo get() requiere una clave como primer argumento. Como segundo argumento
#opcional, puedes pasar el valor a retornar si la calve no existe:

valor_puntos = alien_0.get('puntos', 'No hay un valor asignado.')
print(valor_puntos)

#De esta manera obtendremos una respuesta en vez de un error
#Si existe la posibilidad de que la clave por la que estas buscando pueda no
#existir, considera usar el metodo get() en vez de la notacion de los parentesis
#cuadrados.
#Si no pones el segundo argumento dentro del metodo get() Python retornara el
#valor None, lo que significa "Ningun valor existe", lo cual no es un error,
#mas bien es un valor especial que significa ausencia de valor.

