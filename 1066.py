contador = [0] * 4
palavras = ["par(es)", "impar(es)", "positivo(s)", "negativo(s)"]
for i in range(0, 5):
    x = int(input())
    
    if x % 2 == 0:
        contador[0] += 1
    if x % 2 != 0:
        contador[1] += 1
    if x > 0:
        contador[2] += 1
    if x < 0:
        contador[3] += 1
        
for i in range(0,4):
    print(f"{contador[i]} valor(es) {palavras[i]}")

