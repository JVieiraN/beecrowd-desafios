"""
Admito que quando se trata de problemas com tempo eu tenho uma certa dificuldade,
principalmente quando me obrigo a não usar uma biblioteca como foi no exemplo
anterior.
"""

hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

inicio_minutos = hora_inicial * 60 + minuto_inicial
fim_minutos = hora_final * 60 + minuto_final

if fim_minutos < inicio_minutos:  
    fim_minutos += 24 * 60
else:
    if fim_minutos == inicio_minutos:
        fim_minutos += 24 * 60  

duracao_total = fim_minutos - inicio_minutos
horas = duracao_total // 60
minutos = duracao_total % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")