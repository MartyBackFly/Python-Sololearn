def concatenate_example(n):
    if n == 0:
        return "0"
    else:
        return concatenate_example(n - 1) + str(n) 


n = int(input("numero here -->"))
result = concatenate_example(n)
print(result)

print ("-------------------------------------------")


def concatenate_example(n):
    if n == 0:
        return "0"
    else:
        return concatenate_example(n - 1) + str(n) + str("-")


n = int(input("numero here -->"))
result = concatenate_example(n)
print(result)

