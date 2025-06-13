teste = 1 
num_bilhetes = 1
while num_bilhetes != 0:
    num_bilhetes = int(input())
    if num_bilhetes == 0:
        break
    bilhetes = input()
    lista_bilhetes = bilhetes.split()
    for i in range(1, num_bilhetes + 1):
        if int(lista_bilhetes[i - 1]) == i:
            print(f'Teste {teste}')
            print(i)
            print()
            break
    teste += 1
