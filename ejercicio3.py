#Dada la matriz 3×3: [[1,2,3],[4,5,6],[7,8,9]] — 
# Calcular y mostrar la suma de cada fila y 
# la suma de cada columna.

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]
]

for i in range (len(matriz)):
    suma_filas = sum(matriz[i])
    print (f"fila {i+1} = {suma_filas}")


for j in range(len(matriz[0])):
    suma_columna = 0
    for i in range(len(matriz)):
        suma_columna += matriz[i][j]
    print(f"Columna {j + 1}: {suma_columna}")