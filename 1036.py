import math
def bhaskara(a, b = 0, c = 0):
    delta = (b**2) - (4*a*c)
    if a == 0 or delta < 0:
        return "Impossivel calcular"
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    return [x1, x2]
    
x, y, z = map(float, input().split())

resultado = bhaskara(x, y, z)

if type(resultado) is not str:
    for i in range(len(resultado)):
        print(f"R{i+1} = {resultado[i]:.5f}")
else:
    print(resultado)