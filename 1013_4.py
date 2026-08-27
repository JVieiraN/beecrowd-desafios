"""Resultado para quando só sei de matemática"""

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
maior = ((a+b+abs(a-b))/2)
maior_de_todos = int((maior+c+abs(abs(maior)-c))/2)
print(f"{maior_de_todos} eh o maior")