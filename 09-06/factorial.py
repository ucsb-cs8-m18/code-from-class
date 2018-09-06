# "fac" is factorial

def fac_recursively(N):
    if N <= 1:
        return 1
    else:
        return N * fac_recursively(N-1)

def fac_iteratively(N):
    product = 1
    for i in range(N, 1, -1):
        product = product * i
    return product

print(fac_recursively(5))
print(fac_iteratively(5))