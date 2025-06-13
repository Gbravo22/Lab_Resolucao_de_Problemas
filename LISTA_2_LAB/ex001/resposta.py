while True:
    contadorA = 0
    contadorB = 0
    N = int(input())
    if N == 0:
        break
    for i in range (0, N):
        valores = list(map(int,input().split()))
        A = valores[0]
        B = valores[1]
        if A > B:
            contadorA = contadorA + 1
        if B > A: 
            contadorB = contadorB + 1
        else:
            continue
    print(contadorA,contadorB)
