a, b, c = map(int, input().split())
original = [a,b,c]
lista = sorted(original)
total = lista + [""] + original

for item in total:
    print(item)