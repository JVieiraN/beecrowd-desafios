numeros = []
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    z = x+y
    nova_string = ''
    for caractere in str(z):
        if caractere == "0":
            continue
        nova_string += caractere
    numeros.append(nova_string)
for numero in numeros:
    print(int(numero))
    
