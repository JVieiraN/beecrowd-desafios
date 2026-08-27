"""Resultado para quando não sei da existência da função max e nem de map"""

a, b, c = input().split()
a, b, c = [int(a), int(b), int(c)]
def maior(x, y):
    maior = (x+y+abs(x-y))/2
    return int(maior)

maior_a_b = maior(a, b)
maior_maior_c = maior(maior_a_b, c)
print(f"{maior_maior_c} eh o maior")