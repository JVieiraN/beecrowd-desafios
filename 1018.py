numero = int(input())
mostrar = numero
cedulas = []

cedulas.append(f"{numero // 100} nota(s) de R$ 100,00")
numero %= 100

cedulas.append(f"{numero // 50} nota(s) de R$ 50,00")
numero %= 50

cedulas.append(f"{numero // 20} nota(s) de R$ 20,00")
numero %= 20

cedulas.append(f"{numero // 10} nota(s) de R$ 10,00")
numero %= 10

cedulas.append(f"{numero // 5} nota(s) de R$ 5,00")
numero %= 5

cedulas.append(f"{numero // 2} nota(s) de R$ 2,00")
numero %= 2

cedulas.append(f"{numero // 1} nota(s) de R$ 1,00")

print(mostrar)
for res in cedulas:
    print(res)