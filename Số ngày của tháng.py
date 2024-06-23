a, b = map(int, input().split())
if a >= 1 and a <= 12 and b > 0:    
    if b % 400 == 0 or ( b % 4 == 0 and b % 100 != 0):
        if a in (1, 3, 5, 7, 8, 10, 12):
            print('31')
        elif a == 2:
            print('29')
        else:
            print('30')
    else:
        if a in (1, 3, 5, 7, 8, 10, 12):
            print('31')
        elif a == 2:
            print('28')
        else:
            print('30')
else:
    print('INVALID')
