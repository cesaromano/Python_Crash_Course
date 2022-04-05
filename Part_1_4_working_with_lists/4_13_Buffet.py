#piensa en 5 comidas basicas y almacenalas en un tuple
comidas = ('pasta', 'rabioli', 'churrasco', 'ensalada', 'papas fritas')
#usa un loop for para imprimir cada comida 
for comida in comidas:
	print(f"\n{comida.title()}")
#intenta cambiar uno de los items y asegurate que Python rechace el cambio
#comidas.append('cualquier basura')
#grega una nueva linea que reemplace el menu con dos comidas diferentes y luego usa el loop for
#para imprimir las comidas
comidas = ('pasta', 'mazamorra paisa', 'churrasco', 'rellena', 'papas fritas')
for comida in comidas:
	print(f"\n{comida.title()}")

#	CORRIGIENDO EL ESTILO DE TU CODIGO
#Haz tu codigo que sea lo mas facil de leer, escribir un codigo facil de leer 
#esto ayudara a mantener seguimiento de lo que tu codigo hace y le ayudara a otros 
#a entender tu codigo
#Programadores de Python ese han puesto de acuerdo con un numero de convensiones de estilo
#para asegurarse de que el codigo de todos sea estructurado aproximadamente del mismo estilo

#*La guia de estilo
#Cuando alguien quiere realizar un cambio al lenguaje de Python 
#escribimos a Python Enhacement Proposal (PEP) uno de los mas viejos
#es el PEP 8 que instruye a los programadores de Python acerca del estilo de programacion 
#Dar la opcion entre escribir codigo que es facil de escribir o codigo que es facil de leer. 
#los programadores de Python casi siempre te animaran a escribir un codigo que sea facil de leer
#las siguientes guias te ayudaran a escribir un codigo mas claro desde el principio

#*Identation
#PEP8 Recomienda que uses 8 espacios por nivel de identacion. usando cuatro espacios 
#se mejora la legibilidad mientras que se deja espacio para multiples espacios de identacion
#para cada linea.
#El editor de texto debe proveer la opcion de editar la cantidad de espacios que se desea
#por cada tab, usar espacios y tab en el mismo codigo genera problemas que aveces son
#dificiles de diagnosticar

#*Longitud de la linea
#Muchos programadores de Python recomiendan que cada linea deberia contener menos de 80 caracteres
#Programadores profesionales a menudo tienen varios archivos abiertos en la misma pantalla
#una linea de 80 caracteres le permite ver lineas enteras con dos o tres archivos abiertos
#paralelamente.
#PEP8 tambien recomienda que la longitud de un comentario deberia ser de 72 caracteres por linea
#por que algunas de las herramientas que generan documentacion automaticamente
#para largos proyectos agregan caracteres de formato al principio de cada linea.

#*Lineas en blanco
#Para agrupar partes de tu programa visualmente, se usan lineas blancas.
#Deberias utilizar lineas blancas para organizar tus archivos, pero no lo hagas excesivamente
#no deberian utilizarse dos o tres lineas blancas entre dos secciones
#las lineas blancas no afectan como corre el codigo, si no que afectan la
#legibilidad del codigo

#*Otras guias de estilo
#PEP8 tiene recomendaciones adicionales de estilo, pero muchas de estas
#se refieren a programas mas complejos.