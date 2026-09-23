# Realiza: (1) Agregar "Pedro Ruiz", (2) Buscar "Carlos Díaz" y
# mostrar posición, (3) Modificar "Luis Torres" por "Luis Mendoza",
# # (4) Eliminar "Ana García".

# (1) Agregar "Pedro Ruiz"
agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
agenda.append("Pedro Ruiz")

# (2) Buscando a Carlos Diaz
def buscar (agenda, persona):
    for i, valor in enumerate(agenda):
        if valor == "Carlos Díaz":
            return valor,i

pos = buscar (agenda, "Carlos Díaz")
print (f"Busqueda: {pos}")

# (3) Modificar Luis Torres por Luis Mendoza
agenda[1] = "Luis Mendoza"

#(4) Eliminar Ana Garcia
agenda.remove ("Ana García")

print (agenda)

        
