from datetime import datetime

dia_inicial = input().split(" ")
dia_inicial = int(dia_inicial[1])
h_i, m_i, s_i = map(int, input().split(":"))
dia_final = input().split(" ")
dia_final = int(dia_final[1])
h_f, m_f, s_f = map(int, input().split(":"))

ini = datetime(2026, 4, dia_inicial, h_i, m_i, s_i)
fim = datetime(2026, 4, dia_final, h_f, m_f, s_f)

diferenca = fim - ini
dias = diferenca.days
segundos_restantes = diferenca.seconds
horas = segundos_restantes // 3600
minutos = (segundos_restantes % 3600) // 60
segundos = segundos_restantes % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")