"""
Tentei varias vezes fazer esse exercício usando ponto flutuante, porém quando
se chega na parte do 1 centavo, a lógica falha por um erro de precisão do
próprio python, por isso, aproveitei o código do arquivo 1018 e transformei
todos os valores em inteiros para garantir a precisão do programa
"""


valor = float(input())
mostrar = valor
numero = int(round(valor * 100))
cedulas = []
moedas = []

cedulas.append(f"{numero // 10000} nota(s) de R$ 100.00")
numero %= 10000

cedulas.append(f"{numero // 5000} nota(s) de R$ 50.00")
numero %= 5000

cedulas.append(f"{numero // 2000} nota(s) de R$ 20.00")
numero %= 2000

cedulas.append(f"{numero // 1000} nota(s) de R$ 10.00")
numero %= 1000

cedulas.append(f"{numero // 500} nota(s) de R$ 5.00")
numero %= 500

cedulas.append(f"{numero // 200} nota(s) de R$ 2.00")
numero %= 200

# Moedas (valores em centavos)
moedas.append(f"{numero // 100} moeda(s) de R$ 1.00")
numero %= 100

moedas.append(f"{numero // 50} moeda(s) de R$ 0.50")
numero %= 50

moedas.append(f"{numero // 25} moeda(s) de R$ 0.25")
numero %= 25

moedas.append(f"{numero // 10} moeda(s) de R$ 0.10")
numero %= 10

moedas.append(f"{numero // 5} moeda(s) de R$ 0.05")
numero %= 5

moedas.append(f"{numero // 1} moeda(s) de R$ 0.01")

print("NOTAS:")
for res in cedulas:
    print(res)

print("MOEDAS:")
for res in moedas:
    print(res)