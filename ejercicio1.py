# #Dado el siguiente arreglo de 
# notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
# Escribir un programa que calcule: promedio, nota más alta, 
# nota más baja y cuántos aprobaron (nota ≥ 11).

notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]

def calc_prom (notas):
    return sum(notas) / len(notas)

nota_alta = max(notas)
nota_baja = min(notas)
promedio = calc_prom(notas)
aprobados = 0

for i in notas:
    if i >= 11:
        aprobados += 1

print (f"{promedio:.2f}")
print (f"La nota mas baja es: {nota_baja}")
print (f"La nota mas alta es: {nota_alta}")
print (f"Aprobaron {aprobados} alumnos")

