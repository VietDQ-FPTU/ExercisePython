from math import *
a, b, c= map(float, input().split())
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
