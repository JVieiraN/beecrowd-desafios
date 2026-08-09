numero = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())
salario = horas_trabalhadas * valor_por_hora
#Se tentar quebrar a linha com \n o beecrowd não vai aceitar...
print(f'NUMBER = {numero}')
print(f'SALARY = U$ {salario:.2f}')
