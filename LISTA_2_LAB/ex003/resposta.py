num = list(map(int,input().split()))
inicial = num[0]
operações = num[1]
D = inicial
E = inicial 
F = inicial
for i in range(0, operações):
    op = list(input().split())
    if op[0] != 'A':
        operacao = op[0]
        nome = op[1]
        valor = int(op[2])
    else:
        operacao = op[0]
        recebedor = op[1]
        pagador = op [2]
        valor = int(op[3])
        if recebedor == 'D':
            D = D + valor
            if pagador == 'E':
                E = E - valor
            if pagador == 'F':
                F = F - valor
        elif recebedor == 'E':
            E = E + valor
            if pagador == 'D':
                D = D - valor
            if pagador == 'F':
                F = F - valor
        else:
            F = F + valor
            if pagador == 'D':
                D = D - valor
            if pagador == 'E':
                E = E - valor
    if operacao == 'C':
        if nome == 'E':
            E = E - valor 
        if nome == 'D':
            D = D - valor 
        if nome == 'F':
            F = F - valor 
    if operacao == 'V':
        if nome == 'E':
            E = E + valor 
        if nome == 'D':
            D = D + valor 
        if nome == 'F':
            F = F + valor 
print(D,E,F)
