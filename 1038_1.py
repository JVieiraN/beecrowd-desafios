total = 0
codigo = list(range(1,6))
preco = [4, 4.5, 5, 2, 1.5]

x, y = map(int, input().split())

for i in range(len(codigo)):
    if x == codigo[i]:
        total += y * preco[i]
        break
        
print(f"Total: R$ {total:.2f}")