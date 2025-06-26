def somarlista(lista,maior):
    n = len(lista)
    soma = 0
    for i in range(0,n):
        soma = soma + lista[i]
    if soma > maior:
        maior = soma
        return maior
    else:
        return maior
vertical, horizontal = list(map(int,input().split()))
todaslistas = []
maior = -1
for i in range(0,vertical):
    listaatual = list(map(int,input().split()))
    todaslistas.append(listaatual)
for j in range(0,vertical):
    maior = somarlista(todaslistas[j],maior)

for i in range(0,horizontal):
    soma = 0
    for h in range(0,vertical):
        soma = soma + todaslistas[h][i]
    if soma > maior:
        maior = soma
    else:
        continue
print(maior)
