#import pizza

#pizza.hacer_pizza(30, 'pepperoni')
#pizza.hacer_pizza(25, 'mushroom', 'green peppers', 'extra cheese')

#Cuando Python lee este archivo, la linea import pizza le dice a Python que abra 
#el archivo pizza.py y copie todas las funciones de ese programa en este programa.
#No puedes ver en realdiad el codigo siendo copiado entre los archivos por que 
#Python copia el codigo detras de escena justo antes de que el programa corra.
#Todo lo que necesitas saber es que cualquier funcion definida dentro de pizza.py
#estara disponible en este programa.
#Para llamar la funcion desde un modulo importado, ingresa el nombre del modulo 
#que importaste, seguido por el nombre de la funcion, make_pizza(), separado por un
#punto. Este codigo produce el mismo output que el programa original del que se 
#importo el modulo.
#Este primer enfoque de importacion, en el cual tu simplemente escribes importe
#seguido de el nombre del modulo, hace cada funcion desde el modulo disponible
#en tu programa. Si usas este tipo de declaracion import para importar un modulo
#entero, cada funcion en el modulo esta disponible por medio de la siguiente 
#sintaxis:

#module_name.function_name()

#*Importando funciones especificas
#Puedes tambien importar una funcion especifica desde un modulo. Esta es la sitaxis
#general para este enfoque:

#form module_name import function_name

#Puedes importar cuantas funciones quieras desde un modulo separando cada nombre
#de funcion con coma:

#from module_name import function_0, function_1, function_2

#from pizza import hacer_pizza

#hacer_pizza(30, 'pepperoni')
#hacer_pizza(25, 'mushroom', 'green peppers', 'extra cheese')

#Con esta sintaxis no necesitas usar la notacion del punto cuando llamas una funcion. 
#Por que tenemos explicitamente importada la funcion hacer_pizza() en la declaracion
#import, podemos llamarla por su nombre cuando usamos la funcion.

#*Usando as para dar un alias a una funcion
#Si el nombre de una funcion que tu estas importando puede entrar en conflicto con
#un nombre existente en tu programa o si el nombre de la funcion es largo, puedes
#usar un corto y unico alias, un nombre alternativo similar para un nickname 
#desde la funcion.

#from pizza import hacer_pizza as hp 

#hp(30, 'pepperoni')
#hp(25, 'mushroom', 'green peppers', 'extra cheese')

#La declaracion import muestra aqui el renombre de la funcion hacer_pizza() a mp()
#en este programa. Cada vez que queramos llamar hacer_pizza() podemos simplemente
#escribir hp() en vez de esto.
#la sintaxis general para preoveer un alias es:

#from module_name import function_name as fn

#*Usando as para dar un alias a un modulo
#Puedes tambien proveer un alias al nombre de un modulo. dandole a un modulo un 
#alias corto, como p para pizza, permitiendote llamar la funcion del modulo mas
#rapidamente.

#import pizza as p

#p.hacer_pizza(30, 'pepperoni')
#p.hacer_pizza(25, 'mushroom', 'green peppers', 'extra cheese')

#Esta manera no solo es mas concisa si no que tambien direcciona tu atencion del 
#nombre del modulo. Esos nombres de funciones que claramente te dicen lo que 
#cada funcion son mas importantes para la legibilidad de tu codigo que usar el
#nombre completo de la funcion.
#La sintaxis general para este enfoque es:

#import module_name as mn

#*Importando todas las funciones en un modulo
#Puedes decirle a Python que importe cada funcion en un modulo usando el operador
#asterisco (*)

from pizza import *

hacer_pizza(16, 'pepperoni')
hacer_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

#El asterisco en la declaracion de importacion le dice a Python que copie cada 
#funcion desde el modulo pizza en este archivo de programa. Como cada funcion es
#importada, puedes llamar cada funcion por el nombre sin usar la notacion del punto
#Sin embargo es mejor no usar este enfoque cuando estas trabajando con modulos
#grandes que no has escrito: si el modulo tiene un nombre de funcion que coincida 
#con un nombre existente en tu proyecto, puedes tener resultados inesperados.

#El mejor modo es importar la funcion o funciones que quieres, o importar el 
#modulo entero y usar la notacion del punto. Esto permite un codigo limpio que es
#facil de leer y entender:

#from module_name import *

#*Estilo de las funciones
#Las funciones deben tener nombres descriptivos, y esos nombres usar letras 
#minusculas y guiones bajos. Nombres descriptivos te ayudaran a ti y a los demas
#a entender que es lo que trata de hacer tu codigo. Los nombres de los modulos
#tambien deberian usar esa convencion tambien.
#Cada funcion debe tener un comentario que explique concisamente que hace la funcion.
#Este coentario debera aparecer inmediatamente despues de la definicion de la 
#funcion y usar el formato "docstring". En una funcion bien documentada otros 
#programadores pueden usar la funcion leyendo solo la descripcion en el "docstring"
#Ellos deberan asegurarse de que el codigo trabaje como es descrito, y a medida
#que es sea largo sepan el nombre de la funcion, el argumento que sea necesario
#y el tipo de valor que retorne, deberan ser capaces de usarlo en sus programas.
#Si tu especificas un valor por defecto para un parametro, no deben ser usados 
#espacios en ningun lado del signo igual:

#def function_name(parameter_0, parameter_1='default value')

#La misma convencion debera ser usada para argumentos keyword en llamadas de funcion:

#fuction_name(value_0, parameter_1='value')

#PEP8 recomeinda que limitar los caracteres en las lineas de codigo a 79, asi
#cada linea es visible en en tamaño razonable de la ventana de editor. Si un 
#conjunto de parametros causa que la definicion de la funcion sea mayor a 79 
#caracteres, presiona enter despues de abrir el parentesis en la linea de definicion.
#En la siguiente linea, presiona "TAB" dos veces para separa la lista de los
#argumentos desde el cuerpo de la funcion, el cual solo sera identado un nivel.
#La mayoria de los editores de codigo automaticamente ajusta cualquier linea
#adicional de parametros para identificar la identacion que has establecido en la
#primera linea:

#def function_name(
#		parameter_0, parameter_1, parameter_2,
#		parameter_3, parameter_4, parameter_5):
#	function body...  

#Si tu programa o modulo tiene tiene mas de una funcion puedes separar cada una
#por medio de dos lineas blancas para hacer mas facil de ver donde inicia una
#funcion y donde termina la otra.
#Todas las declaraciones import deberan ser escritas al comienzo de un archivo.
#La unica excepcion es si tu usas comentarios al comienzo de tu archivo para
#escibir el programa general.