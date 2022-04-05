def imprimir_modelos(sin_imprimir, impresos):
	"""
	Simula impresion de cada diseño, hasta que ninguno falte.
	Mueve cada diseño  a modelos_completados despues de impresos.
	"""
	while sin_imprimir:
		impresion_actual = sin_imprimir.pop()
		print(f"Imprimiendo modelo: {impresion_actual}")
		impresos.append(impresion_actual)

def mostrar_modelos_completos(impresos):
	"""Muestra todas las impresiones completas"""
	print("\nLos siguientes modelos han sido impresos:")
	for impreso in impresos:
		print(impreso)

#sin_imprimir = ['retenedor de telefono', 'manija', 'dedo']
#impresos = []
#imprimir_modelos(sin_imprimir[:], impresos)
#mostrar_modelos_completos(impresos)