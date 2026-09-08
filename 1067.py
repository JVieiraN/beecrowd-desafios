x = int(input())
numeros = list(range(0,x))
if x % 2 != 0:
    numeros = list(range(0,x+1))
for numero in numeros:
    if numero % 2 != 0:
        print(numero)

