#Comienza programando desde el ejercicio anterior
people_dinner = ['cesar', 'einstein', 'freddie']
print(f"Querido {people_dinner[0].title()}, estas cordialmente invitado a cenar hoy a las 7pm")
print(f"Querido {people_dinner[1].title()}, estas cordialmente invitado a cenar hoy a las 7pm")
print(f"Querido {people_dinner[2].title()}, estas cordialmente invitado a cenar hoy a las 7pm")
#Escribe una frase de alguno de los invitados que no puede asistir
print(f"Querido {people_dinner[0].title()}, es una pena que no puedas asistir a la cena")
#Modifica la lista reemplazando el nombre del invitado que no puede asistir
#con el nombre de una nueva persona a la que quieres invitar
invitado_removido = people_dinner.remove('cesar')
people_dinner.insert(0, 'julio')
print(f"Querido {people_dinner[0].title()}, estas cordialmente invitado a cenar hoy a las 7 pm")
print(f"Querido {people_dinner[1].title()}, estas cordialmente invitado a cenar hoy a las 7 pm")
print(f"Querido {people_dinner[2].title()}, estas cordialmente invitado a cenar hoy a las 7 pm")