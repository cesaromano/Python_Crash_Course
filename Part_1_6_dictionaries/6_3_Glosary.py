#Un diccionario de Python puede usarse para modelar un diccionario real.
#sin embargo para evitar confusiones, lo llamaremos glosario.
#Piensa en cinco palabras de programacion que has aprendido, en capitulos
#anteriores, usa esas palabras como claves en tu glosario y almacna su 
#significado como valores.

glosario = {
	'identar' : 'Correr cuatro espacios hacia la derecha',
	'loop' : 'Funcion para repetir un fragmeto de codigo de programacion',
	'if' : 'Declaracion que se usa para realizar una accion dependiendo de un estado, informacion de tipo booleano',
	'variable' : 'Informacion asociada a un nombre',
	'string' : 'Tipo de informacion que se caracteriz por estar entre comillas',
}

print(f"Identar:\n\t{glosario['identar']}.")
print(f"\nLoop:\n\t{glosario['loop']}.")
print(f"\nIf:\n\t{glosario['if']}.")
print(f"\nVariable:\n\t{glosario['variable']}.")
print(f"\nString:\n\t{glosario['string']}.")