"""Resultado para quando sou completamente iniciante"""

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
maior_a_b = (a+b+abs(a-b))/2
maior_maior_c = int((maior_a_b+c+abs(maior_a_b-c))/2)
print(f"{maior_maior_c} eh o maior")