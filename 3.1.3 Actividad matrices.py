
matriz = [[0 for _ in range(4)] for _ in range(3)]

for i in range(3):
    for j in range(4):
        matriz[i][j] = int(input(f"Ingrese el elemento en la posición [{i}][{j}]: "))

print("\nMatriz 3x4:")
for fila in matriz:
    print(" ".join(map(str, fila)))


colores = [
    [["amarillo", "rojo", "Naranja"], ["Verde", "Blanco", "amarillo"], ["rojo", "Verde", "Naranja"]],
    [["Blanco", "amarillo", "Verde"], ["rojo", "Naranja", "Blanco"], ["amarillo", "rojo", "Verde"]],
    [["Naranja", "Verde", "Blanco"], ["amarillo", "rojo", "Naranja"], ["Verde", "Blanco", "amarillo"]]
]

contadores = {"amarillo": 0, "rojo": 0, "Naranja": 0, "Verde": 0, "Blanco": 0}

for capa in colores:
    for fila in capa:
        for color in fila:
            contadores[color] += 1

print("\nNúmero de elementos de cada color:")
for color, cantidad in contadores.items():
    print(f"{color}: {cantidad}")


bus = [[(i * 4) + j + 1 for j in range(4)] for i in range(10)]

print("\nAsientos del bus:")
for fila in bus:
    print(" ".join(map(str, fila)))
