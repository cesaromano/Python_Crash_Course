#*Copiando una lista
#A menudo se querra comenzar con una lista y hacer nuevas listas basadas en esta 
#examinaremos como se hace y cuan util puede ser
#para copiar la lista se puede hacer un slice de toda la lista omitiendo los dos indices [:]
mis_comidas = ['carne', 'burritos', 'lassagna', 'torta de maiz']
amigo_comidas = mis_comidas [:]

print("Mis comidas favoritas son:")
print(mis_comidas)

print("\n Las comidas favoritas de mi amigo son:")
print(amigo_comidas)
#a copia se realizo tomando un slice de toda la lista de mis_comidas
#para probar que se obtuvieron dos listas, se adiere una nueva comida a cada una

mis_comidas.append('chorizo')
amigo_comidas.append('arepa')

print("Mis comidas favoritas son:")
print(mis_comidas)

print("\n Las comidas favoritas de mi amigo son:")
print(amigo_comidas)

#Esto no habria funcionado de haber puesto la lista de mi amigo
#igual a la mie

#amigo_comidas = mis_comidas

#mis_comidas.append('chorizo')
#amigo_comidas.append('arepa')

#print("Mis comidas favoritas son:")
#print(mis_comidas)

#print("\n Las comidas favoritas de mi amigo son:")
#print(amigo_comidas)

#en este caso las dos variables refieren a la misma lisa
#como resultado los nuevos items agregados se asocian a las dos variables
#siendo este un error logico

