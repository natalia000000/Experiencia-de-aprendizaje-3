import csv
import json

def clasificar_empresa(ventas):
    if ventas <= 100000000:
        return "Pequeño Contribuyente"
    elif ventas <= 200000000:
        return "Mediano Contribuyente"
    else:
        return "Gran Contribuyente"

archivo_csv = "listadoRutEmpresa.csv"
archivo_json = "segmentacionEmpresas.json"

empresas = []
with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rut = row['rut']
        nombre = row['nombre']
        ventas = int(row['ventas'])
        clasificacion = clasificar_empresa(ventas)
        
        row['clasificacionEmpresa'] = clasificacion
        
        empresas.append(row)

with open(archivo_json, 'w', encoding='utf-8') as jsonfile:
    json.dump(empresas, jsonfile, indent=4, ensure_ascii=False)

print(f"Se ha creado el archivo {archivo_json} satisfactoriamente.")
