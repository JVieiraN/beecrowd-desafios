n = int(input())
intervalo = list(range(1,10000 + 1))
for numero in intervalo:
    if numero % n == 2:
        print(numero)