lanches = {
    1: 4,
    2: 4.5,
    3: 5,
    4: 2,
    5: 1.5
}

codigo, quantidade = map(int, input().split())
total = lanches.get(codigo) * quantidade
print(f"Total: R$ {total:.2f}")