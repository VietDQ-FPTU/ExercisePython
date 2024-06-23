from math import *
a, b, c, d = map(int,input().split())
if  (b%a==0)and b*b/a==c and c*b/a==d:
    print('YES')
else : print ('NO')