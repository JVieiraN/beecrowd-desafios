x = int(input())
numeros = list(range(x,x+12))
if x % 2 != 0:
    numeros = list(range(x-1,x+12))
for numero in numeros:
    if numero % 2 != 0:
        print(numero)