

# Explicación:

# __name__ es una variable especial en Python que toma diferentes valores dependiendo 
# de cómo se está utilizando el script.

# Cuando el script se ejecuta directamente (como un programa principal), __name__ tiene el valor "__main__". 
# Por lo tanto, el bloque de código dentro del if __name__ == "__main__": se ejecutará solo en este caso.

# Si el script se importa como un módulo en otro script, __name__ tomará el nombre del módulo
# y el bloque dentro del if no se ejecutará.

# En resumen, esta construcción se utiliza para incluir código que solo debe ejecutarse 
# cuando el script se está ejecutando directamente y no cuando se importa como un módulo 
# en otro script. En tu caso actual, como la línea está comentada, el bloque de código 
# se ejecutará siempre, independientemente de cómo se ejecute el script.


def espacio():
    print ("")
    print ("---------------------")
    print ("")
if __name__ == "__main__":
 espacio()


