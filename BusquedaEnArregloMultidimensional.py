# Matriz 3x3 con valores numéricos
matriz = [
    [5, 8, 2],
    [1, 9, 3],
    [4, 7, 6]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor_buscado):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor_buscado:
                print(f"✅ Valor {valor_buscado} encontrado en la posición [{fila}][{columna}]")
                return
    print(f"❌ Valor {valor_buscado} no encontrado en la matriz")

# Valor que quieres buscar
valor = int(input("Ingresa el valor que deseas buscar: "))
buscar_valor(matriz, valor)