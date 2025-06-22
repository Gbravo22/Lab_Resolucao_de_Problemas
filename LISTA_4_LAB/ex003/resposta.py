def encontrarvogais(palavra):
    vogais = "aeiou"
    lista_vogais = []
    for i in range(0,len(palavra)):
        if palavra[i] in vogais:
            lista_vogais.append(palavra[i])
        else:
            continue
    return lista_vogais
palavra = str(input())
lista = encontrarvogais(palavra)
def verificar_risada(lista, verificar = True, i = 0, f = len(lista) - 1):
    if i >= f:
        return verificar
    else:
        if lista[i] ==  lista[f]:
            return verificar_risada(lista, verificar = True, i = i + 1, f = f - 1)
        else:
            return False
verificacao = verificar_risada(lista)
if verificacao == True:
    print("S")
else:
    print("N")
