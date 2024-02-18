

""" #Definir función
def bmi(weight, height):
  index = weight / (height * height)
  return index  #sends the return value back



#Llamando a una función y usando el valor de retorno
Vero = bmi(61, 1.83) #stores return value
print("Vero ""underweight:", Vero < 18.5)

#Otra llamada
Sol = bmi(75, 1.74)
print("Sol " "underweight:", Sol < 18.5) """

""" 
weight = int(input("cuanto pesas ? ---> "))
height = float(input("cuanto medis ? ---> "))

def bmi(weight, height):
  index = weight / (height * height)
  if index < 18.5 : 
   print("Tenes Sobrepeso" + "BMI -->" + index) 
  else : 
    print("No Tenes Sobrepeso " + "BMI -->" + index)
  
  
  return index  #sends the return value back """



weight = float(input("¿Cuánto pesas? ---> "))
print()
height = float(input("¿Cuánto mides? (en metros EJ: 1.70 ) ---> "))
print()
def bmi(weight, height):
    index = weight / (height * height)
    if index <= 18.5:
        #texto formateado con f 
        print(f"No Tienes Sobrepeso - BMI --> {index}")
    else:
        #texto formateado old school str()
        print("Tienes Sobrepeso - BMI --> " + str(index))

    return index

bmi_value = bmi(weight, height)


print("------------------")


