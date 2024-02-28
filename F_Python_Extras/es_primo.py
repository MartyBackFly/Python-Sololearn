
print()
print ("vamos a chekear si son primos los numeros que esten entre los valores que ingreses")

def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    #your code goes here
    for i in range(a, b):
      if isPrime(i):
        yield i  

print()
f = int(input("desde en numero -->"))
print()
t = int(input("hasta el numero -->"))

  

print(list(primeGenerator(f, t)))





#misma pero de chat gpt 

def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n == 0:
            return False
    return True

def primeGenerator(a, b):
    for num in range(a, b + 1):
        if isPrime(num):
            yield num

f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))


print()

# Usando range(a, b + 1) para incluir b
for i in range(3, 8 + 1):
    print(i)

print()

# No usando range(a, b + 1) para no incluir b
for i in range(3, 8 ):
    print(i)

print()