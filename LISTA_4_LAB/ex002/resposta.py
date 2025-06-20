def verificar(y,acao):
    if acao == "LEFT":
        return y - 1
    if acao == "RIGHT":
        return y + 1
n_testes = int(input())
for i in range(0,n_testes):
    y = 0
    lista_acoes = []
    n_instrucoes = int(input())
    for j in range (0,n_instrucoes):
        acao = input().split()
        if len(acao) == 1:
            lista_acoes.append(acao[0])
            y = verificar(y,acao[0])
        else:
            acao = acao[2]
            acao = int(acao) - 1
            acao1 = lista_acoes[acao]
            lista_acoes.append(acao1)
            y = verificar(y,acao1)
    print(y)
