bandejas = int(input())
derrubados = 0
for i in range(0,bandejas):
    LC = list(map(int,input().split()))
    L = LC[0]
    C = LC[1]
    if L > C:
        derrubados = derrubados + C
print(derrubados)
