notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
aprobados = 0

promedio =sum(notas) / len(notas)
nota_max = max(notas)
nota_min = min(notas)

for nota in notas:
    if nota >= 11:
        aprobados += 1

print(f"Promedio = {promedio} / Max = {nota_max} / Min = {nota_min} / Aprobados = {aprobados}")