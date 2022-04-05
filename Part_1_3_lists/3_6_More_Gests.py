#Comienza programando desde el ejercicio anterior
people_dinner = ['cesar', 'einstein', 'freddie']
invitado_removido = people_dinner.remove('cesar')
people_dinner.insert(0, 'julio')
#Envia un mensaje a cada invitado diciendo que ampliaras la mesa
#print(f"Querido {people_dinner[0].title()}, te escribo para informarte que he fundado una mesa mas grande para la cena")
#print(f"Querido {people_dinner[1].title()}, te escribo para informarte que he fundado una mesa mas grande para la cena")
#print(f"Querido {people_dinner[2].title()}, te escribo para informarte que he fundado una mesa mas grande para la cena")
#Agrega nuevos invitas
people_dinner.insert(0, 'rosalba')
people_dinner.insert(3, 'victor')
people_dinner.append('sergio')
#Envia un nuevo mensaje a todos los invitados
print(f"Querido {people_dinner[0].title()}, te escribo para informarte que he fundado una mesa mas grande para la cena")
print(f"Querido {people_dinner[1].title()}, te escribo para informarte que he fundado una mesa mas grande para la cena")
print(f"Querido {people_dinner[2].title()}, te escribo para informarte que he fundado una mesa mas grande para la cena")
print(f"Querido {people_dinner[3].title()}, te escribo para informarte que he fundado una mesa mas grande para la cena")
print(f"Querido {people_dinner[4].title()}, te escribo para informarte que he fundado una mesa mas grande para la cena")
print(f"Querido {people_dinner[5].title()}, te escribo para informarte que he fundado una mesa mas grande para la cena")
