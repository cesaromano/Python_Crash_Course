#Coloca las funciones del ejemplo printing models en un archivo separado llamado
#printing_functions.py. Escribe una declaracion import al comienzo de printing_models 
#y modifica el archivo para usar las funciones importadas

import printing_functions as pf 

sin_imprimir = ['retenedor de telefono', 'manija', 'dedo']
impresos = []

pf.imprimir_modelos(sin_imprimir[:], impresos)
pf.mostrar_modelos_completos(impresos)