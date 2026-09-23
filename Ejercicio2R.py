# Ejercicio 2 - Operaciones CRUD en Agenda de contactos

agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]

agenda.append("Pedro Ruiz")

agenda[1]= "Luis Mendoza"

agenda.remove("Ana García")

posicion = agenda.index("Carlos Díaz")

print(agenda)
print(f"Carlos Díaz está en la posición {posicion + 1}")