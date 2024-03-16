def cuenta_atras(numero):
    numero -= 1 
    if numero > 0:
       print(numero)
       cuenta_atras(numero)
    else:
       print("-----------")
       print(f"orden de liberacion {numero}")
    #print(f"orden de liberacion {numero}")
cuenta_atras(12)

print ("------------------------------------------------")


def cuenta_atras(numero):
    numero -= 1 
    if numero > 0:
       print(numero)
       cuenta_atras(numero)
    else:
       print("-----------")
       #print(f"orden de liberacion {numero}")
    print(f"orden de liberacion {numero}")
cuenta_atras(12)


print ("------------------------------------------------")


def sumaRecursiva(num):
   if num == 1:
      return 1
   else:
      return num + sumaRecursiva(num - 1)


#resultado = sumaRecursiva(10)   

print(f"resultado suma recursiva {sumaRecursiva(5) } ")

# la funcion primero hace lo de la izq -num- 

#  5 + algo que no se aun 
#  4 + algo que no se aun
#  3 + algo que no se aun
#  2 + algo que no se aun
#  1 (si es 1 -- > return 1 )

#  retorna 1 y comienzo a subir para atras  2 + 1  = 3 -- > 3 + 3 = 6 --> 4 + 6 = 10 -- > 5 + 10 = 15 :D

print ("------------------------------------------------")


def fact(num):
   if num == 1:
    return 1 
   else:
      return num * fact(num - 1)
   

print(fact(5))


#  5 x algo que no se aun 24

#  4 x algo que no se aun 6

#  3 x algo que no se aun 2

#  2 x algo que no se aun 1

#  1 (si es 1 -- > return 1 )

#  retorna 1 y comienzo a subir para atras  2 * 1  = 2 -- > 3 * 2 = 6 --> 4 * 6 = 24 -- > 5 * 24 = 120 :D

print ("------------------------------------------------2")

def mostrarLista(lista, index): 
   if index != len(lista):
      print(lista[index])
      mostrarLista(lista, index+1) 

lista = [1,2,3,4,5,6,7,8,9]

mostrarLista(lista, 5)
print ("------------")
mostrarLista(lista, 8)
print ("------------")
mostrarLista(lista, 2)

print ("------------------------------------------------")

