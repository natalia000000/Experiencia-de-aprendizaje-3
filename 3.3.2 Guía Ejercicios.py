#ejercicio 1
import csv
import json

archivo_csv = 'datos.csv'
archivo_json = 'mayores.json'

mayores = []

def determinar_edad(edad):
    if edad >= 25:
        return "Mayor"
    else:
        return "Menor"

with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nombre = row['Nombre']
        edad = int(row['Edad'])
        comuna = row['Comuna']
        
        estado_edad = determinar_edad(edad)
        
        print(f"Nombre: {nombre}, Edad: {edad}, Estado: {estado_edad}, Comuna: {comuna}")
        
        if edad >= 25:
            mayores.append(row)

with open(archivo_json, 'w', encoding='utf-8') as jsonfile:
    json.dump(mayores, jsonfile, indent=4, ensure_ascii=False)

print(f"\nSe ha creado el archivo {archivo_json} satisfactoriamente con los mayores de 25 años.")


#ejercicio 2
import csv
import json

archivo_csv = "listadoRun.csv"
archivo_json = "ganadores.json"

def es_ganador(rut):
    ultimos_digitos = rut[-3:-1]
    return ultimos_digitos in ['92', '95', '84']

ganadores = []

with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rut = row['run']
        nombre = row['nombre']
        
        if es_ganador(rut):
            ganadores.append({'run': rut, 'nombre': nombre})

with open(archivo_json, 'w', encoding='utf-8') as jsonfile:
    json.dump(ganadores, jsonfile, indent=4, ensure_ascii=False)

print(f"Se ha creado el archivo {archivo_json} satisfactoriamente con los RUTs ganadores.")
