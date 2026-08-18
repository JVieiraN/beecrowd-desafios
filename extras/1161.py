import math

respostas = []
while True:
    try:
        m, n = input().split()
        m = math.factorial(int(m))
        n = math.factorial(int(n))
        respostas.append(m+n)
    except EOFError:
        for i in range(len(respostas)):
            print(respostas[i])
        break