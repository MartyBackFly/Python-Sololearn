
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


print("------------------")
print("------------------")


def obtener_peso():
    while True:
        try:
            weight = float(input("¿Cuánto pesas? (en kilos  EJ: 76 )---> "))
            return weight
        except ValueError:
            print("Error: Ingresa un valor numérico para el peso.")

def obtener_altura():
    while True:
        try:
            height = float(input("¿Cuánto mides? (en metros EJ: 1.67 ) ---> "))
            return height
        except ValueError:
            print("Error: Ingresa un valor numérico para la altura.")



def bmi(weight, height):
    index = weight / (height * height)

    # Redondear el BMI a 2 decimales
    rounded_index = round(index, 2)



    if index < 18.5:
        #texto formateado con f 
        print(f"Tenes exeso de flacura - BMI --> {rounded_index}")
    
    elif index >= 18.5 and index <= 24.9:
        #texto formateado con f 
        print(f" Estas exelente  - BMI --> {rounded_index}")
    
    elif index >= 25.0 and index <= 29.9:
        #texto formateado old school str()
        print("Tenes que aflojarle al morfi  - BMI --> " + str(rounded_index))
    else:
        #texto formateado old school str()
        print("Estas hecho una gorda inmunda  - BMI --> " + str(rounded_index))

    return rounded_index


# Obtener peso y altura con validación de entrada
height= obtener_altura()

print("------------------")

weight = obtener_peso()

print("------------------")


# almaceno el valor en bmi_value por si lo quiero usar ... 
# podria solo llamar a la funcion solo usando -- >bmi(weight, height) 

bmi_value = bmi(weight, height)




print("------------------")


#Peso inferior al normal	Menos de 18.5
#Normal	18.5 – 24.9
#Peso superior al normal	25.0 – 29.9
#Obesidad	Más de 30.0


