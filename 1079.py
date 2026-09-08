n = int(input())
pesos = [2,3,5]
respostas = []
for i in range(n):
    numeros = input().split()
    for j in range(3):
        numeros[j] = float(numeros[j]) * pesos[j]
    media = sum(numeros)/sum(pesos)
    respostas.append(f"{media:.1f}")
for resposta in respostas:
    print(resposta)