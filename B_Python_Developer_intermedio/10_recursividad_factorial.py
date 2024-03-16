from imprimir import espacio as aa
aa()


def cuenta_atras(numero):
    numero -= 1 
    if numero > 0:
       print(numero)
       cuenta_atras(numero)
    else:
       print("asdasd")
    print(f"orden de liberacion {numero}")
    

cuenta_atras(12)


aa()

def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)
    
print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))
print(factorial(10))

# 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). 
# Para aplicar esto de forma recursiva, observa que 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, 2! = 2 * 1 . 
# Por lo general,, n! = n * (n-1)!.


aa()


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 6
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")




aa()

# La expresión 6!=6×5!, 5!=5×4, 5!=5×4, y así sucesivamente, 
# sigue la lógica recursiva que mencionaste. Cada llamada a la función factorial se reduce 
# al problema más pequeño hasta llegar al caso base, donde N es 0 o 1, y se devuelve 1.

#En el ejemplo con n=6, la secuencia de llamadas recursivas sería:


#  6!=6×5!
#  5!=5×4!
#  4!=4×3!
#  3!=3×2!
#  2!=2×1!
#  1!=1×0!

# Dado que 0!=1, las llamadas recursivas se resuelven hacia atrás y se obtiene el resultado final 6!=720


def is_even(x): #par 
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x): #impar
  return not is_even(x)


print(is_odd(4))
print(is_even(6))


# Vamos a seguir el ejemplo de la pila de llamadas para la función is_odd(4) y ver cómo se llama a la función is_even y se resuelve:

# is_odd(4) llama a is_even(3)
# is_even(3) llama a is_odd(2)
# is_odd(2) llama a is_even(1)
# is_even(1) llama a is_odd(0)
# is_odd(0) devuelve True (caso base)
# Ahora, comenzamos a resolver las llamadas en la pila:

# is_even(1) devuelve not is_odd(0), y como is_odd(0) es True, entonces is_even(1) devuelve not True, que es False.
# is_odd(2) devuelve False (resultado de is_even(1))
# is_even(3) devuelve not is_odd(2), y como is_odd(2) es False, entonces is_even(3) devuelve not False, que es True.
# is_odd(4) devuelve True (resultado de is_even(3))
# Por lo tanto, el resultado final de print(is_odd(4)) será True.

# Ahora, para is_even(6):

# is_even(6) llama a is_odd(5)
# is_odd(5) llama a is_even(4)
# is_even(4) llama a is_odd(3)
# is_odd(3) llama a is_even(2)
# is_even(2) llama a is_odd(1)
# is_odd(1) llama a is_even(0)
# is_even(0) devuelve True (caso base)
# Ahora, comenzamos a resolver las llamadas en la pila:

# is_odd(1) devuelve not is_even(0), y como is_even(0) es True, entonces is_odd(1) devuelve not True, que es False.
# is_even(2) devuelve not is_odd(1), y como is_odd(1) es False, entonces is_even(2) devuelve not False, que es True.
# is_odd(3) devuelve True (resultado de is_even(2))
# is_even(4) devuelve not is_odd(3), y como is_odd(3) es True, entonces is_even(4) devuelve not True, que es False.
# is_odd(5) devuelve False (resultado de is_even(4))
# is_even(6) devuelve not is_odd(5), y como is_odd(5) es False, entonces is_even(6) devuelve not False, que es True.
# Por lo tanto, el resultado de print(is_even(6)) es True.


aa()

def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)

print(fib(4))
print(" fibonacci de 4 ")

aa()
print("-=-=-=-=-=-")
def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
print(fib(7))


aa()



#sololearn ejercicio 
def convert(decimal_number):
    if decimal_number == 0:
        return "0"
    elif decimal_number == 1:
        return "1"
    else:
        return convert(decimal_number // 2) + str(decimal_number % 2)

# Solicitar entrada al usuario
decimal_input = int(input("pone numerito -->"))

# Llamar a la función convert() e imprimir el resultado
binary_result = convert(decimal_input)
print(binary_result)


aa()



# con extras de chat GPT 



