
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

numero = int(input("Ingrese un número para calcular la serie de Fibonacci recursivo: "))
resultado = fibonacci_recursivo(numero)
print("El resultado de la serie de Fibonacci para n =", numero, "es:", resultado,  "recursivo")


#orden de ejecucion exponencial: O(2^n)
    
def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

numero = int(input("Ingrese un número para calcular la serie de Fibonacci iterativo: "))
resultado = fibonacci_recursivo(numero)
print("El resultado de la serie de Fibonacci para n =", numero, "es:", resultado, "iterativo")


#orden de ejecucion lineal: O(n ) 


#----------------------------------------------------------------

#  Fibonacci(0) = 0
# Fibonacci(1) = 1
# Fibonacci(2) = Fibonacci(1) + Fibonacci(0) = 1 + 0 = 1
# Fibonacci(3) = Fibonacci(2) + Fibonacci(1) = 1 + 1 = 2
# Fibonacci(4) = Fibonacci(3) + Fibonacci(2) = 2 + 1 = 3
# Fibonacci(5) = Fibonacci(4) + Fibonacci(3) = 3 + 2 = 5
# Fibonacci(6) = Fibonacci(5) + Fibonacci(4) = 5 + 3 = 8
# Fibonacci(7) = Fibonacci(6) + Fibonacci(5) = 8 + 5 = 13 



# 2 en 1 

""" def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

numero = int(input("Ingrese un número para calcular la serie de Fibonacci: "))

# Usar el enfoque recursivo
resultado_recursivo = fibonacci_recursivo(numero)
print("Resultado (recursivo) para n =", numero, "es:", resultado_recursivo)

# Usar el enfoque iterativo
resultado_iterativo = fibonacci_iterativo(numero)
print("Resultado (iterativo) para n =", numero, "es:", resultado_iterativo) """