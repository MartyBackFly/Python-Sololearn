numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)  # Salida: [2, 4, 6, 8]

print ("-------------------------------")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 8, 8, 8, 8, 88]
numeros_pares = list(map(lambda x: x % 2 == 0, numeros))
print(numeros_pares)  # Salida: [2, 4, 6, 8]