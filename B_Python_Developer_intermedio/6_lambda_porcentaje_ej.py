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