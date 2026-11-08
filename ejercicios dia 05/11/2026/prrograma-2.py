# Solicitar el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz: "))

# Crear la matriz
matriz = []

# Llenar la matriz usando ciclos
for i in range(n):
    fila = []
    for j in range(n):
        valor = int(input(f"Ingrese el valor [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# Imprimir la matriz
print("\nMatriz resultante:")
for i in range(n):
    for j in range(n):
        print(matriz[i][j], end=" ")
    print()