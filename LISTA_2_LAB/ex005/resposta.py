nota = int(input())
if nota == 0:
    print('E')
elif nota > 1 and nota <36:
    print('D')
elif nota > 35 and nota <61:
    print('C')
elif nota > 60 and nota < 86:
    print('B')
else: 
    print('A')
