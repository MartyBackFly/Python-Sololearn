from aafuncionimprimir import espacio as aa



import time

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def medir_tiempo_ejecucion(func, *args):
    inicio_tiempo = time.time()
    resultado = func(*args)
    fin_tiempo = time.time()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    return resultado, tiempo_ejecucion

# Ejemplo de uso para la función recursiva
numero_recursivo = int(input("Ingrese un número para calcular la serie de Fibonacci recursivo: "))
resultado_recursivo, tiempo_recursivo = medir_tiempo_ejecucion(fibonacci_recursivo, numero_recursivo)
print("El resultado de la serie de Fibonacci para n =", numero_recursivo, "es:", resultado_recursivo, "recursivo")
print("Tiempo de ejecución para Fibonacci recursivo:", tiempo_recursivo, "segundos")

aa()

# Ejemplo de uso para la función iterativa
numero_iterativo = int(input("Ingrese un número para calcular la serie de Fibonacci iterativo: "))
resultado_iterativo, tiempo_iterativo = medir_tiempo_ejecucion(fibonacci_iterativo, numero_iterativo)
print("El resultado de la serie de Fibonacci para n =", numero_iterativo, "es:", resultado_iterativo, "iterativo")
print("Tiempo de ejecución para Fibonacci iterativo:", tiempo_iterativo, "segundos")
