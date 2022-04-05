#Escribe un loop que le diga al usuario que ingrese una serie de adiciones de pizza
#hasta que ingrese el valor 'salir', cuando ingrese las adiciones, imprime un 
#mensaje que diga has agregado esata adicion a tu pizza:

prompt = "\nIngresa la adicion que deseas agregar a tu pizza: "
prompt += "\nSi ya terminaste escribe 'salir'"
adicion = ""

while adicion != 'salir':
	adicion = input(prompt)
	print(f"\nHas agregado la adicion {adicion.title()} a tu pizza!")
