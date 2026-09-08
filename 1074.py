x = int(input())
respostas = []
def mais_menos(num):
    if num > 0:
        return "POSITIVE"
    return "NEGATIVE"
def par_impar(num):
    if num % 2 == 0:
        return "EVEN"
    return "ODD"

for i in range(x):
    numero = int(input())
    if numero != 0:
        palavra = par_impar(numero) + " " + mais_menos(numero)
    else: 
        palavra = "NULL"
    respostas.append(palavra)

for resposta in respostas:
    print(resposta)