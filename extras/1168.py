numeros = [
{"numero": 0, "leds": 6},
{"numero": 1, "leds": 2},
{"numero": 2, "leds": 5},
{"numero": 3, "leds": 5},
{"numero": 4, "leds": 4},
{"numero": 5, "leds": 5},
{"numero": 6, "leds": 6},
{"numero": 7, "leds": 3},
{"numero": 8, "leds": 7},
{"numero": 9, "leds": 6}
    ]

def contador(valor_listado):
    contador_de_leds = 0
    for n in valor_listado:
        for dicionario in numeros:
            if int(n) == dicionario["numero"]:
                contador_de_leds += dicionario["leds"]
    return f"{contador_de_leds} leds"
    

casos = int(input())
colecao = []
for i in range(casos):
    n = input().strip()
    n = list(n)
    res = contador(n)
    colecao.append(res)

for resposta in colecao:
    print(resposta)