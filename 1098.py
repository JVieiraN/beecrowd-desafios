for i in range(0, 22, 2):
    I = i / 10
    for k in range(3):
        J = (i / 10) + k + 1
        if i % 10 == 0:
            print(f"I={I:.0f} J={J:.0f}")
        else:
            print(f"I={I:.1f} J={J:.1f}")
