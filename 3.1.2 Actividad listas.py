#Ejercicio 1
nombres = []
for i in range(3):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    nombres.append(nombre)


nombre_mas_largo = max(nombres, key=len)


print(f"El nombre con mayor cantidad de caracteres es: {nombre_mas_largo}")


#Ejercicio 2
nombres = []
apellidos = []

for i in range(3):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    nombres.append(nombre)


for i in range(3):
    apellido = input(f"Ingrese el apellido {i+1}: ")
    apellidos.append(apellido)

print("\nNombres y apellidos ingresados:")
for i in range(3):
    print(f"{nombres[i]} {apellidos[i]}")



#Ejercicio 3
nombres = []

while True:
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    continuar = input("¿Desea agregar otro nombre? (si/no): ")
    if continuar.lower() == "no":
        break

nombre_mas_corto = min(nombres, key=len)
nombres.remove(nombre_mas_corto)

print("\nLista de nombres después de eliminar el nombre con menos caracteres:")
for nombre in nombres:
    print(nombre)


#Ejercicio 4
usuarios = {}

def registrar_usuario():
    username = input("Ingrese nombre de usuario: ")
    if username in usuarios:
        print("El nombre de usuario ya está registrado.")
        return
    password = input("Ingrese contraseña: ")
    usuarios[username] = password
    print("Usuario registrado exitosamente.")

def iniciar_sesion():
    username = input("Ingrese nombre de usuario: ")
    password = input("Ingrese contraseña: ")
    if username in usuarios and usuarios[username] == password:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

def eliminar_usuario():
    username = input("Ingrese el nombre de usuario a eliminar: ")
    if username not in usuarios:
        print("El nombre de usuario no existe.")
        return
    password = input("Ingrese la contraseña: ")
    if usuarios[username] == password:
        del usuarios[username]
        print("Usuario eliminado exitosamente.")
    else:
        print("Contraseña incorrecta.")

def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

mostrar_menu()



#Ejercicio 5
productos = {
    "1. Manzana": 1.0,
    "2. Pan": 2.5,
    "3. Leche": 1.5,
    "4. Huevos": 3.0,
    "5. Queso": 4.0
}

canasta = []

def agregar_productos():
    print("\nLista de productos:")
    for producto, precio in productos.items():
        print(f"{producto} - ${precio}")
    
    opcion = input("Seleccione el número del producto que desea agregar: ")
    
    if opcion == "1":
        canasta.append(("Manzana", productos["1. Manzana"]))
    elif opcion == "2":
        canasta.append(("Pan", productos["2. Pan"]))
    elif opcion == "3":
        canasta.append(("Leche", productos["3. Leche"]))
    elif opcion == "4":
        canasta.append(("Huevos", productos["4. Huevos"]))
    elif opcion == "5":
        canasta.append(("Queso", productos["5. Queso"]))
    else:
        print("Opción inválida. Por favor, seleccione un producto válido.")

def ver_canasta():
    if not canasta:
        print("\nLa canasta está vacía.")
    else:
        print("\nProductos en la canasta:")
        for producto, precio in canasta:
            print(f"{producto} - ${precio}")

def ver_total():
    total = sum(precio for _, precio in canasta)
    print(f"\nEl total a pagar es: ${total:.2f}")

def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1. Agregar productos")
        print("2. Ver canasta")
        print("3. Ver total")
        print("4. Salir")
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            agregar_productos()
        elif opcion == "2":
            ver_canasta()
        elif opcion == "3":
            ver_total()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

mostrar_menu()
