# ejercicio 1
informacion = ("Juan", 30, "Ciudad de México")

print("Acceso por índices:")
print("Nombre:", informacion[0])
print("Edad:", informacion[1])
print("Ciudad:", informacion[2])

nombre, edad, ciudad = informacion

print("\nDesempaquetado de tupla:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)


#ejercicio 2
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

suma_total = sum(numeros)
print("Suma de los elementos:", suma_total)

maximo = max(numeros)
minimo = min(numeros)
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)

cantidad_cinco = numeros.count(5)
print("Número de veces que aparece el 5:", cantidad_cinco)


#ejercicio 3
letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

primeras_cinco = letras[:5]
print("Primeras 5 letras:", primeras_cinco)

ultimas_tres = letras[-3:]
print("Últimas 3 letras:", ultimas_tres)

cada_segunda = letras[::2]
print("Cada segunda letra:", cada_segunda)

