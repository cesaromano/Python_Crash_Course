#	LOOPING EN UN DICCIONARIO
#Debido a que un diccionario puede puede contener grandes cantidades de 
#informacion, Python permite hacer loop en el, ademas existen diferentes 
#maneras de hacerlo. Puedes hacer loop en los pares de claves-valores, en las
#claves o en los valores.

#*Haciendo loop en todos los pares claves-valores
#Consideremos un diccionario diseñado para almacenar informacion acerca de un 
#usuario en un sitio web:

user_0 = {
	'nombre de usuario' : 'metebolas',
	'nombre' : 'machaca',
	'apellido' : 'huevos',
}

#para ver cada una de las informaciones del diccionario puedes usar el loop for
#a por el diccionario:

for key, value in user_0.items():
	print(f"\nClave: {key}")
	print(f"Valor: {value}")

#se pueden crear nombres para las dos variables que almacenaran la clave y su 
#valor de cada par clave-valor, puedes elegir los nombres que quieras para esas
#dos variables, funciona tambien con abreviaciones para el nombre de la variable.
#el resto del ciclo contiene el metodo item(), que retorna la lista de los pares
#clave-valor, el loop luego asigna cada uno de esos pares a las dos variables.

#Este tipo de loop funciona bien si tu diccionario almacena los resultados
#de una encuesta de miles o millones de personas.