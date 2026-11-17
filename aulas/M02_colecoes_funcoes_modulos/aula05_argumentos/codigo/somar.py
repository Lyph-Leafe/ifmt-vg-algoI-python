def somar(*numeros):
    print("Recebi:", numeros)
    return sum(numeros)


print(somar(2, 3))
print(somar(1, 2, 3, 4, 5))
