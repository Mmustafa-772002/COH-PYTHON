def fact(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

print(fact(5))

def fact(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
f = fact(5)
print(f)