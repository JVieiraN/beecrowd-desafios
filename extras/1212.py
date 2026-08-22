"""De todos os desafios, esse com certeza foi o mais divertido, foi uma resposta totalmente desenvolvida a base de gambiarras kkkkkkkkkk"""

resultados = []
while True:
    a,b = input().split()
    if a == "0" and b == "0":
        break
    if len(b) > len(a):
        a, b = b, a
    if len(b) < len(a):
        b = ('0'*(len(a)-len(b))) + b
    a = list(a)
    b = list(b)
    a = [int(i) for i in a]
    b = [int(j) for j in b]
    tamanho_listas = len(a)

    carry = 0
    for i in range(tamanho_listas - 1, -1, -1):
        if a[i] + b[i] >= 10:
            if i > 0:
                a[i-1] += 1
                carry += 1
            else:
                carry += 1
    resultados.append(carry)

for resultado in resultados:
    if resultado == 0:
        print("No carry operation.")
    elif resultado == 1:
        print(f"{resultado} carry operation")
    else:
        print(f"{resultado} carry operations")
