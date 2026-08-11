numero_de_linhas = int(input())

pares = []
impares = []
for i in range(0, numero_de_linhas):
    numeros = int(input())
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

pares.sort()
impares.sort(reverse=True)
total = pares + impares

for i in range(0, len(total)):
    print(total[i])