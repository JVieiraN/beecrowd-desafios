a, b, c = map(float, input().split())
lados = [a,b,c]
condicao1 = a < (b+c)
condicao2 = b < (a+c)
condicao3 = c < (a+b)

if condicao1 and condicao2 and condicao3:
    print(f"Perimetro = {sum(lados):.1f}")
else:
    trapezio = ((a+b) * c)/2
    print(f"Area = {trapezio:.1f}")
    