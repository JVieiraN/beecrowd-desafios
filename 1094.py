animais= {
    "c": 0,
    "r": 0,
    "s": 0
}

total = 0
casos = int(input())
for i in range(casos):
    quantidade, animal = input().split()
    quantidade = int(quantidade)
    animais[animal.lower()] += quantidade
    total += quantidade

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {animais['c']}")
print(f"Total de ratos: {animais['r']}")
print(f"Total de sapos: {animais['s']}")
print(f"Percentual de coelhos: {((100 * animais['c'])/total):.2f} %")
print(f"Percentual de ratos: {((100 * animais['r'])/total):.2f} %")
print(f"Percentual de sapos: {((100 * animais['s'])/total):.2f} %")