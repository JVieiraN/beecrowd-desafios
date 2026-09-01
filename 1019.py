segundos_dados = int(input())
horas = segundos_dados // 3600
resto = segundos_dados - horas * 3600
minutos = resto // 60
segundos = resto % 60
formato = f"{horas}:{minutos}:{segundos}"
print(formato)