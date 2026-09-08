x = int(input())
y = int(input())
if x > y:
    x, y = y, x

soma = 0
for numero in range(x + 1, y):
    if numero % 2 != 0:
        soma += numero

print(soma)