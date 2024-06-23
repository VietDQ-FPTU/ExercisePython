from math import *
a, b = map(int, input().split())
print(a + b, a - b, a * b,sep = '\n', end = '\n')
if b == 0:
    print('INVALID')
else:
    print('%.4f' % (a / b))
