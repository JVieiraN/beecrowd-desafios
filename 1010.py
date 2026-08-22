codigo1, quantidade1, valor1 = input().split()
codigo2, quantidade2, valor2 = input().split()

#INTEIRO X FLOAT VAI DAR FLOAT DO MESMO JEITO, ENTÃO AS QUANTIDADES NÃO PRECISAM SER INTEIRAS
quantidade1, quantidade2, valor1, valor2 = map(float, [quantidade1, quantidade2, valor1, valor2])
pagar = (quantidade1 * valor1) + (quantidade2 * valor2)
print(f"VALOR A PAGAR: R$ {pagar:.2f}")