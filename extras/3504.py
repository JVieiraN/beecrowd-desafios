frase = input()
frase = list(frase)
nova_frase = frase[::-1]

def comparar(a, b):
    if a == b:
        return True
    return False

if comparar(frase, nova_frase) == True:
    frase = ''.join(frase)
    print(f"A frase [{frase}] eh palindrome")
else:
    frase = ''.join(frase)
    print(f"A frase [{frase}] nao eh palindrome")