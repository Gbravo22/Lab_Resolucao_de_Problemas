a = int(input())
b = int(input())
if a%2 == 0 and b%2 != 0:
    print('0')
elif a%2 != 0 and b%2 == 0:
    print('0')
else:
    print('1')
