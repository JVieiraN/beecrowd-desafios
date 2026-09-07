peso = [2,3,4,1]
n1, n2, n3, n4 = map(float, input().split())
notas = [n1, n2, n3, n4]
somatorio_com_pesos = 0

for i in range(len(peso)):
    somatorio_com_pesos += peso[i] * notas[i]

media = somatorio_com_pesos/sum(peso)

if media >= 7:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media < 5:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
elif media >= 5 and media <= 6.9:
    exame = float(input())
    total = (media+exame)/2
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    print(f"Nota do exame: {exame:.1f}")
    if total >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {total:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {total:.1f}")

