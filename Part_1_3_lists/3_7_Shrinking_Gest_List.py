#Comienza programando desde el ejercicio anterior
people_dinner = ['cesar', 'einstein', 'freddie']
invitado_removido = people_dinner.remove('cesar')
people_dinner.insert(0, 'julio')
people_dinner.insert(0, 'rosalba')
people_dinner.insert(3, 'victor')
people_dinner.append('sergio')
#Envia un mensaje diciendoles a todos que solo puedes invitar a dos personas a la cena
#print(f"{people_dinner[0].title()}, lamento comunicarte que solo podre invitar a dos personas a la cena. Lo siento")
#print(f"{people_dinner[1].title()}, lamento comunicarte que solo podre invitar a dos personas a la cena. Lo siento")
#print(f"{people_dinner[2].title()}, lamento comunicarte que solo podre invitar a dos personas a la cena. Lo siento")
#print(f"{people_dinner[3].title()}, lamento comunicarte que solo podre invitar a dos personas a la cena. Lo siento")
#print(f"{people_dinner[4].title()}, lamento comunicarte que solo podre invitar a dos personas a la cena. Lo siento")
#print(f"{people_dinner[5].title()}, lamento comunicarte que solo podre invitar a dos personas a la cena. Lo siento")
#Usa el metodo pop para remover invitados de tu lista una a la 
#vez menos dos nombres que quieres que permanescan en la lista
#cada vez que remuevas a una persona de la lista hasle saber que ha sido
#retirado de la lista
invitado_1 = people_dinner.pop(2)
#print(f"{invitado_1.title()}, lamento informarte que fuiste removido de la lista, sera para la proxima amigo")
invitado_2 = people_dinner.pop(2)
#print(f"{invitado_2.title()}, lamento informarte que fuiste removido de la lista, sera para la proxima amigo")
invitado_3 = people_dinner.pop(2)
#print(f"{invitado_3.title()}, lamento informarte que fuiste removido de la lista, sera para la proxima amigo")
invitado_4 = people_dinner.pop(2)
#print(f"{invitado_4.title()}, lamento informarte que fuiste removido de la lista, sera para la proxima amigo")
#Escribe un mensaje a cada una de las dos personas que 
#continuan en tu lista, hasles saber que continuan invitadas
print(f"{people_dinner[0].title()}, me place comunicarte que nuestra cena sigue en pie")
print(f"{people_dinner[1].title()}, me place comunicarte que nuestra cena sigue en pie")
#Usa del para remover los ultimos dos nombres de tu lista
#Imprime la lista para estar seguro de que esta vacia
print(people_dinner)
del people_dinner[0]
del people_dinner[0]
print(people_dinner)