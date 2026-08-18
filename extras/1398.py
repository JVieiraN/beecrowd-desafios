molde = ["0b"]
N = 131071
numeros = []

def remover_espacos(lista):
    for char in lista:
        if char == ' ':
            lista.remove(' ')
    return lista

while True:
    try:
        adicionar = input()
        adicionar = remover_espacos(list(adicionar))
        molde = molde + adicionar
        if molde[-1] == '#':
            molde.pop()
            binario = ''.join(molde)
            binario = int(binario, 2)
            adicionar = []
            molde = ["0b"]
            numeros.append(binario)
    except EOFError:
        for numero in numeros:
            if numero % N == 0:
                print("YES")
            else:
                print("NO")
        break