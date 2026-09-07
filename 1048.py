x = float(input())
limites = [
    x >= 0 and x <= 400,
    x >= 400.01 and x <= 800,
    x >= 800.01 and x <= 1200,
    x >= 1200.01 and x <= 2000,
    x > 2000
    ]

percentuais = [15, 12, 10, 7, 4]

for i in range(len(limites)):
    if limites[i]:
        reajuste = x * (percentuais[i] / 100)
        salario_novo = x + reajuste
        
        print(f"Novo salario: {salario_novo:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print(f"Em percentual: {percentuais[i]} %")