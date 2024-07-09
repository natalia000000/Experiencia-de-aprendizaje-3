#ejercicio 1
def validar_numero(mensaje):
    while True:
        try:
            valor = input(mensaje)
            numero = float(valor)  
            return numero
        except ValueError:
            print("Error: Ingrese un número válido.")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b

def main():
    num1 = validar_numero("Ingrese el primer número: ")
    num2 = validar_numero("Ingrese el segundo número: ")
    
    print("\nSeleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = input("Ingrese el número de la operación deseada (1/2/3/4): ")
    
    if opcion == '1':
        resultado = sumar(num1, num2)
        print(f"\nResultado de la suma: {resultado}")
    elif opcion == '2':
        resultado = restar(num1, num2)
        print(f"\nResultado de la resta: {resultado}")
    elif opcion == '3':
        resultado = multiplicar(num1, num2)
        print(f"\nResultado de la multiplicación: {resultado}")
    elif opcion == '4':
        resultado = dividir(num1, num2)
        print(f"\nResultado de la división: {resultado}")
    else:
        print("\nOpción no válida. Por favor, seleccione una opción válida (1/2/3/4).")

if __name__ == "__main__":
    main()

