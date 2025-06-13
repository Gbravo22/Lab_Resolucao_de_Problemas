maximo = int(input())
num = list(input().split())
a = int(num[0])
b = int(num[2])
op = num[1]
if op == '+':
    resultado = a + b
    if resultado<=maximo:
        print('OK')
    if resultado > maximo:
        print('OVERFLOW')
if op == '*':
    resultado = a * b
    if resultado<=maximo:
        print('OK')
    if resultado > maximo:
        print('OVERFLOW')
