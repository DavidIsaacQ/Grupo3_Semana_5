# Ejercicio 3 - Suma de filas y columnas de una matriz

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

sumaf0 = sum(matriz[0])
sumaf1 = sum(matriz[1]) 
sumaf2 = sum(matriz[2])

sumac0 = matriz[0][0] + matriz[1][0] + matriz[2][0]
sumac1 = matriz[0][1] + matriz[1][1] + matriz[2][1]
sumac2 = matriz[0][2] + matriz[1][2] + matriz[2][2]

print(f"Suma fila 0: {sumaf0} | fila 1: {sumaf1} | fila 2: {sumaf2} || Suma col 0: {sumac0} | col 1: {sumac1} | col 2: {sumac2}")
