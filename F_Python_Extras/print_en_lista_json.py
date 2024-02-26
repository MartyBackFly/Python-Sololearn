import json

personas = [
    {'nombre': 'Alice', 'edad': 25},
    {'nombre': 'Bob', 'edad': 30},
    {'nombre': 'Charlie', 'edad': 20}
]

ordenado_por_edad = sorted(personas, key=lambda x: x['edad'])

# Imprimir la lista como una lista de diccionarios en formato de cadena
print(json.dumps(ordenado_por_edad, indent=2))
