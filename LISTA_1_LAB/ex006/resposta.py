valores = list(map(float, input().split()))
A = valores[0]
G = valores[1]
Ra = valores[2]
Rg = valores[3]
Ca = A/Ra
Cg = G/Rg
if Ca < Cg:
    print("A")
else: 
    print("G")
