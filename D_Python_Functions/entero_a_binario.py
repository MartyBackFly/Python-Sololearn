def convert(decimal_number):
    if decimal_number == 0:
        return "0"
    elif decimal_number == 1:
        return "1"
    else:
        return convert(decimal_number // 2) + str(decimal_number % 2)

# Solicitar entrada al usuario
decimal_input = int(input("pone numerito ej 1 --->"))

# Llamar a la función convert() e imprimir el resultado
binary_result = convert(decimal_input)
print(binary_result)

print("--------------")

decimal_numero = int(input(" pone numerito ej 2--->"))
binario_numero = bin(decimal_numero)

print(f"El número {decimal_numero} en binario es: {binario_numero}")


# 0b indica formato binario 


# Vamos a seguir los mismos pasos para convertir el número decimal 77 a binario:

# 77 ÷ 2 = 38   (residuo: 1)
# 38 ÷ 2 = 19   (residuo: 0)
# 19 ÷ 2 = 9    (residuo: 1)
# 9  ÷ 2 = 4    (residuo: 1)
# 4  ÷ 2 = 2    (residuo: 0)
# 2  ÷ 2 = 1    (residuo: 0)
# 1  ÷ 2 = 0    (residuo: 1)

# Lee los residuos de abajo hacia arriba: 1001101.
# Por lo tanto, 77 en decimal es igual a 1001101 en binario.
