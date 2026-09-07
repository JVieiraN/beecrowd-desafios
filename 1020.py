numero = int(input())
anos = numero // 365
numero = numero % 365
meses = numero // 30
numero = numero % 30
dias = numero

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")