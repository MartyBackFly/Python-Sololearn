

#Definir función
def bmi(weight, height):
  index = weight / (height * height)
  return index  #sends the return value back



#Llamando a una función y usando el valor de retorno
Vero = bmi(61, 1.83) #stores return value
print("Vero ""underweight:", Vero < 18.5)

#Otra llamada
Sol = bmi(75, 1.74)
print("Sol " "underweight:", Sol < 18.5)