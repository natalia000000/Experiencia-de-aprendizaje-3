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

# Solicitar y almacenar 3 nombres y 3 apellidos
for i in range(3):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    apellido = input(f"Ingrese el apellido {i+1}: ")
    nombres.append(nombre)
    apellidos.append(apellido)

# Mostrar de forma ordenada los nombres y apellidos
print("\nNombres:")
for nombre in nombres:
    print(nombre)

print("\nApellidos:")
for apellido in apellidos:
    print(apellido)


#Ejercicio 3
# Crear una lista para almacenar los nombres
nombres = []

# Ciclo para ingresar nombres
while True:
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    
    # Preguntar si desea agregar otro nombre
    respuesta = input("¿Desea agregar otro nombre? (sí/no): ").lower()
    if respuesta != "sí" and respuesta != "si":
        break

if nombres:
    nombre_menor = min(nombres, key=len)
    print(f"\nLista de nombres antes de eliminar el más corto: {nombres}")
    
    # Eliminar el nombre con la menor cantidad de caracteres
    nombres.remove(nombre_menor)
    
    print(f"Nombre eliminado: {nombre_menor}")
    print(f"Lista de nombres después de eliminar el más corto: {nombres}")
else:
    print("No se ingresaron nombres.")
