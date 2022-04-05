
#	9. CLASSES
#Programacion orientada a objetoses uno de los enfoques mas efectivos para
#escribir software. En programacion orientada a objetos escribes classes que
#representan cosas y situaciones del mundo real, y creas objetos basados en esas
#clases. Cuando escribes una clase, defines el comportamiento general que toda la
#categoria de objetos puede tener.
#Cuando creas objetos individuales de las clase, cada objeto es automaticamente
#equipado con el comportamiento general, podras luego dar a cada objeto cualquier
#trato unico que desees. Te sorprendera cuan bien pueden ser modeladas las 
#situaciones del mundo real con la programacion orientada a objetos.
#Hacer un objeto de una clase es llamado "instantiation", y trabajaras con 
#instancias de una clase. En este capitulo escribiras clases y crearas "instances"
#de una clase. Especificaras el tipo de informacion que debera ser almacenada en
#instancias, y definiras acciones que podran ser tomadas con esas instancias.
#Tambien escribiras classes que extiendan la funcionalidad de clases existentes, 
#asi clases similares pueden compartir codigo eficientemente. Almacenaras tus
#classes en modulos e importar classes escritas por otros programadores en tus
#propios programas.
#Entender la programacion orientada a objetos te ayudara a ver el mundo como
#lo hace un programador. Te ayudara a conocer tu codigo, no solo lo que esta
#pasando linea por linea, si no tambien grandes conceptos tras de el. Conociendo
#la logica detras de las clases te entrenara para pensar logicamente de modo que
#puedas escribir programas que efectivamente aborde casi cualquier problema que 
#encuentres.
#Classes tambien te hacen la vida mas facil y los otros programadores con los
#que trabajaras a medida que tomes incrementales desafios complejos. Cuando tu 
#y otros programadores escriben codigo basado en el mismo tipo de logica, seras
#capaz de entender el trabajo de cualquier otro. Tus programas tendran sentido
#para muchos colaboradores, permitiendoles a todos conseguir mas.

#	CREANDO Y USANDO UNA CLASS
#Puedes modelar casi todo usando classes. Comencemos por escribir una clase simple
#Dog, Que sabemos acerca de la mayoria de perros? Tienen nombre y edad. La mayoria
#se sienta y da vueltas. Esas dos piezas de informacion (nombre y edad) y esos
#dos comportamientos (sentarse y dar vuetas) iran en nuestra clase Dog, por que
#son comunes para para la mayoria de perros. Esta clase le dira a Python como
#hacer un objeto que represente un perro. Despues que nuestra clase es escrita, 
#la usaremos para hacer instancias individuales, de las cuales cada una representara
#un perro especifico.

#*Creando la clase Dog
#Cada instancia creada de la clase Dog almacenara un nombre y una edad, y le daremos
#la habilidad a cada perro de sentarse() y da_vueltas():

class Dog:
	"""Un intento de modelar un perro."""

	def __init__(self, name, age):
		"""Inicializar nombres y atributos."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simular un perro sentandose en respuesta a un comando."""
		print (f"{self.name} se esta sentando ahora")

	def roll_over(self):
		"""Simular dar la vuelta en respuesta a un comando."""
		print(f"{self.name} dio la vuelta")

#Por convencion, nombres con mayuscula incial refieren a classes en Python.

#*El metodo __init__()
#Una funcion que hace parte de una clase es un metodo. Todo lo que aprendiste de 
#funciones aplica a metodos tambien; la unica diferencia practica por ahora es
#la forma en la que llamaremos los metodos. El metodo __init__() es un metodo
#especial que Python corre automaticamente siempre que creemos una nueva instancia
#basada en la clase Dog. Este metodo tiene dos guiones bajos al comienzo y dos guiones
#bajos al final, una convencion que ayuda a prevenir nombres por defecto de Phyton
#entren en conflicto con los nombres de tu metodo. Asegurate de usar dos guiones
#bajos a cada lado, si usas solo un guion a cada lado, el metodo no se llamara
#automaticamente cuando usas tu clase, la cual puede resultar en errores que son
#dificiles de identificar.
#El parametro self es requerido en la definicion del metodo, y deberia venir antes
#que cualquier otro parametro. Debera estar incluido en la definicion por que 
#cuando Python llama este metodo luego (para crear una instancia de Dog), el 
#metodo llamara automaticamente pasando el argumento self. Cada metodo llamado
#asociado asociado con una instancia automaticamente pasa self, el cual es una
#referencia a la instancia misma; le da a la instancia individual acceso a los
#atributos y metodos en la clase. Cuando hacemos una isntancia de Dog, Python 
#llamara el metodo __init__() de la clase Dog. Necesitamos pasar un nombre y edad
#como argumentos; self pasara automaticamente, de modo que no necesitaremos pasarlo.
#Siempre que querramos hacer una instancia de la clase Dog, debemos proveer 
#parametros solo para las dos ultimos parametros, nombre y edad.
#Cada variable con el prefijo self esta habilitada para cada metodo en la clase,
#y tambien seremos capaces de acceder esas variables por cualquier instancia 
#creada de la clase.
#Variables que son accesibles por instancias como esta son llamadas attributes.
#La clase Dog tiene otros dos metodos definidos: sit() y roll over(). Por ahora
#las ultimas dos funciones no hacen mucho. Simplemente imprimen un mensaje diciendo
#que el perro se esta sentando o dando vueltas. Pero el concepto puede ser extendido
#a situaciones realisticas: si esta clase fuera escrita para controlar un robot,
#esos metodos podrian dirigir movimientos que causen que un perro robotico se siente
#o de la vuelta.

#*Haciendo una instancia desde una clase
#La clase Dog es un conjunto de instrucciones que le dice a Python como hacer
#instancias individuales representando perros especificos:

my_dog = Dog('Mambo', 3)

print(f"El nombre de mi perro es {my_dog.name}.")
print(f"Mi perro tiene {my_dog.age} años.")

#*Accesando Attributes
#Para Para accesar a atributos se usa la notacion punto. Python mira a la instancia
#my_dog y luego encuentra el nombre del atributo asociado con my_dog. Este es el
#mismo atributo referido en self.name.

#*Metodos de llamada
#Despues de crear una instancia de la clase Dog, podemos usar la notacion del
#punto para llamar cualquier metodo definido en Dog:

my_dog.sit()
my_dog.roll_over()

#Esta sintaxis es muy apropiada cuando a los atributos y metodos se les ha dado
#nombres descriptivos, podemos facilmente inferir lo que un bloque de codigo
#hace.

#*Creando multiples instancias
#Podemos crear cuantas instancias de una clase se necesiten:

your_dog = Dog('Timon', 3)
print(f"\nEl nombre de mi perro es {your_dog.name}.")
print(f"Mi perro tiene {your_dog.age} años.")
your_dog.sit()
your_dog.roll_over()
