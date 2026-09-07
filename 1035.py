a, b, c, d = map(int, input().split())
condicao1 = b > c and d > a
condicao2 = (c+d) > (a+b)
condicao3 = c > 0 and d > 0
condicao4 = a % 2 == 0

if condicao1 and condicao2 and condicao3 and condicao4:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")