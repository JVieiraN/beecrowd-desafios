CARRO = 12
tempo_gasto = int(input())
velocidade_media = int(input())
litros = (velocidade_media/CARRO) * tempo_gasto
print(f"{litros:.3f}")