#([0,25], (25,50], (50,75], (75,100])
def verificar_intervalo(x):
    intervalo1 = x >= 0 and x <= 25
    intervalo2 = x > 25 and x <= 50
    intervalo3 = x > 50 and x <= 75
    intervalo4 = x > 75 and x <= 100
    
    if intervalo1:
        return "Intervalo [0,25]"
    elif intervalo2:
        return "Intervalo (25,50]"
    elif intervalo3:
        return "Intervalo (50,75]"
    elif intervalo4:
        return "Intervalo (75,100]"
    
    return "Fora de intervalo"

x = float(input())

print(verificar_intervalo(x))
