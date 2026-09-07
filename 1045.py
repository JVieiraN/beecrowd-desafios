a, b, c = map(float, input().split())
lista = sorted([a,b,c])[::-1]
a, b, c = lista
respostas = []
if a >= (b+c):
    respostas.append("NAO FORMA TRIANGULO")
else:
    if a**2 == (b**2) + (c**2):
        respostas.append("TRIANGULO RETANGULO")
    elif a**2 > (b**2) + (c**2):
        respostas.append("TRIANGULO OBTUSANGULO")
    elif a**2 < (b**2) + (c**2):
        respostas.append("TRIANGULO ACUTANGULO")
    
    if a == b == c:
        respostas.append("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        respostas.append("TRIANGULO ISOSCELES")
    
for resposta in respostas:
    print(resposta)