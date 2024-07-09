def validar_lista_numeros():
    while True:
        try:
            numeros = input("Ingrese una lista de números enteros separados por espacios: ")
            numeros = numeros.split()
            numeros = [int(num) for num in numeros]  # Convertir todos los elementos a enteros
            return numeros
        except ValueError:
            print("Error: Ingrese únicamente números enteros válidos.")

def identificar_pares_impares(numeros):
    pares = []
    impares = []
    
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    return pares, impares

def mostrar_resultados(pares, impares):
    print("\nNúmeros pares:")
    if pares:
        print(", ".join(map(str, pares)))
    else:
        print("No se encontraron números pares.")
    
    print("\nNúmeros impares:")
    if impares:
        print(", ".join(map(str, impares)))
    else:
        print("No se encontraron números impares.")

def main():
    numeros = validar_lista_numeros()
    pares, impares = identificar_pares_impares(numeros)
    mostrar_resultados(pares, impares)

if __name__ == "__main__":
    main()


