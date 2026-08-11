intervalos = int(input())
soma = 0

for i in range(0, intervalos):
    velocidade, tempo = input().split()
    soma += int(velocidade) * int(tempo)

print(soma)