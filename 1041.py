x,y = map(float, input().split())
q1 = x > 0 and y > 0
q2 = x < 0 and y > 0
q3 = x < 0 and y < 0
q4 = x > 0 and y < 0
origem = x == y == 0
eixox = x != 0 and y == 0
eixoy = x == 0 and y != 0

if q1:
    print("Q1")
elif q2:
    print("Q2")
elif q3:
    print("Q3")
elif q4:
    print("Q4")
elif origem:
    print("Origem")
elif eixox:
    print("Eixo X")
elif eixoy:
    print("Eixo Y")