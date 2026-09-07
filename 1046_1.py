"""
Como o próximo problema é do mesmo tipo desse, então resolvi dar um tiro de canhão
em uma formiga, já para aproveitar no próximo problema...
"""
from datetime import datetime
hora_inicial, hora_final = map(int, input().split())
inicio = datetime(1900, 1, 15, hora_inicial)
fim = datetime(1900, 1, 16, hora_final)
diferenca = fim - inicio
diferenca = diferenca.seconds // 3600

if diferenca == 0:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print(f"O JOGO DUROU {diferenca} HORA(S)")

