from imprimir import espacio as aa

aa()

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

aa()


#   Más métodos mágicos para operadores comunes:
#   __sub__ for -
#   __mul__ for *
#   __truediv__ for /
#   __floordiv__ for //
#   __mod__ for %
#   __or__ for |
#   __pow__ for **
#   __and__ for &
#   __xor__ for ^


# La expresión x + y se traduce en x.__add__(y).
# Sin embargo, si x no ha implementado __add__, y x e y son de tipos diferentes, entonces y.__radd__(x) es llamado.
# Existen métodos r equivalentes para todos los métodos mágicos que acabamos de mencionar.

aa()


class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world ! ! ! ! ")
print(spam / hello)

aa()



class Specialcooking:
    def __init__(self, comida):
        self.comida = comida

    def __add__(self, asd):
        line = "_" * len(asd.comida)
        return "  ++  ".join([self.comida, line, asd.comida])
  

ingrediente1 = (input("ingrediente 1 -- >"))
ingrediente2 = input("ingrediente 1 -- >")
  
recipe = Specialcooking(ingrediente1) 

result = recipe + Specialcooking(ingrediente2)  

print (result)



a1 = Specialcooking("ajo")
a2 = Specialcooking("derse")
print(a1 + a2)