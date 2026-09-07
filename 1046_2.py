"""
ESSE AQUI É O JEITO MAIS CORRETO E LIMPO DE FAZER ESSE PROBLEMA
"""

inicio, fim = map(int, input().split())
diferenca = fim - inicio
if diferenca <= 0:
    diferenca += 24
print(f"O JOGO DUROU {diferenca} HORA(S)")