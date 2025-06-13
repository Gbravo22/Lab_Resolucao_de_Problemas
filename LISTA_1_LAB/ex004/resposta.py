cartas = list(map(int, input().split()))
eh_crescente = False
eh_decrescente = False
if cartas[0]<cartas[1]:
    if cartas[1]<cartas[2]:
        if cartas[2]<cartas[3]:
            if cartas[3]<cartas[4]:
                eh_crescente = True
elif cartas[0]>cartas[1]:
    if cartas[1]>cartas[2]:
        if cartas[2]>cartas[3]:
            if cartas[3]>cartas[4]:
                eh_decrescente = True
if eh_decrescente:
    print('D')
elif eh_crescente:
    print('C')
else:
    print('N')
