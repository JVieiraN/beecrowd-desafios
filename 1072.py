intervalo = list(range(10,21))
x = int(input())
y = 0
z = 0
for i in range(x):
    rep = int(input())
    if rep in intervalo:
        y += 1
    else: 
        z += 1
        
print(f"{y} in")
print(f"{z} out")