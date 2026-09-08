positivos = 0
numeros = []
for i in range(0, 6):
    x = float(input())
    if x > 0:
        positivos += 1
        numeros.append(x)
media = sum(numeros) / len(numeros)
print(f"{positivos} valores positivos")
print(f"{media:.1f}")