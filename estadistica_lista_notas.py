# Dado el siguiente arreglo de notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
# Escribir un programa que calcule: promedio, nota más alta, nota más baja y
# cuántos aprobaron (nota ≥ 11).


notas =  [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]

promedio = sum(notas) / len(notas)
nota_max = max(notas) 
nota_min = min(notas)

aprobados = 0
for n in notas:
    if n >= 11:
        aprobados += 1    
    
        
        
print(f"promedio: {promedio}")
print(f"nota maxima: {nota_max}")
print(f"nota minima: {nota_min}")
print(f"aprobados: {aprobados} de {len(notas)}")

