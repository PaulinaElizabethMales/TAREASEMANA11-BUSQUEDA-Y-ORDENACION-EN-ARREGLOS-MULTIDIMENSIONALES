# Matriz 3x3 con valores numéricos
matriz = [
    [5, 8, 2],
    [1, 9, 3],
    [4, 7, 6]
]

# Función para ordenar una fila usando Bubble Sort
def ordenar_fila(matriz, fila):
    fila_valores = matriz[fila]
    n = len(fila_valores)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila_valores[j] > fila_valores[j + 1]:
                fila_valores[j], fila_valores[j + 1] = fila_valores[j + 1], fila_valores[j]
    matriz[fila] = fila_valores

# Mostrar matriz original
print("📋 Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila deseada
fila_a_ordenar = int(input("Ingresa el número de fila que deseas ordenar (0, 1 o 2): "))
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar matriz con la fila ordenada
print("\n✅ Matriz con la fila ordenada:")
for fila in matriz:
    print(fila)