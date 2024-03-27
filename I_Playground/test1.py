


class Specialcooking:
    def __init__(self, comida):
        self.comida = comida

    def __add__(self, comilona):
        line = "__" * len(comilona.comida)
        return " ".join([self.comida, line, comilona.comida])

# Pedir al usuario los ingredientes
ingrediente1 = input("Ingrediente 1: ")
ingrediente2 = input("Ingrediente 2: ")

# Crear una instancia de la clase Specialcooking
receta = Specialcooking(ingrediente1)

# Usar el operador de suma (+) entre recetas
resultado = receta + Specialcooking(ingrediente2)

print(resultado)

