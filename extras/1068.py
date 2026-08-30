def validar_parenteses(expressao):
    pilha = []
    
    for char in list(expressao):
        if char == "(":
            pilha.append("(")
        elif char == ")":
            if len(pilha) == 0:
                return "incorrect"
            pilha.pop()
        
    if len(pilha) == 0:
        return "correct"
    else:
        return "incorrect"

respostas = []
while True:
    try:
        exp = input()
        respostas.append(validar_parenteses(exp))
    except EOFError:
        break

for resposta in respostas:
    print(resposta)
    
    