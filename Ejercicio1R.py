# Ejercicio 1 - Estadística de una lista de notas

notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]

promedio = sum(notas)/len(notas)

notamax = max(notas)

notamin = min(notas)

aprobados = 0
for i in notas:
    if i >= 11:
        aprobados += 1


print(f"Promedio: {promedio} | Máx: {notamax} | Mín: {notamin} | Aprobados: {aprobados}")

