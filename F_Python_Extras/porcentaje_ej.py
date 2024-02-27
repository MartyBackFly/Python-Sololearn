from imprimir import espacio as aa


price = int(input("price --->"))

perc = int(input("perc --->"))

res = lambda x,y: (x*y)/100

print(round(res(price, perc), 2) )


aa()

price = int(input("price --->"))

perc = int(input("perc --->"))

res = lambda x, y: (x / 100) * y

print(round(res(perc, price), 2))


aa()


# para sacar por ejemplo "si obtengo x monto de tal total cuanto porcentaje es ? seria como la inversa" 

# si de un total de 555 cosas me dieron 143 cosas .. eso que porcentaje de cosas es ? 


price = int(input("price --->"))

perc = int(input("perc --->"))

res = lambda x, y: (x / y) * 100

print(round(res(perc, price), 2))

