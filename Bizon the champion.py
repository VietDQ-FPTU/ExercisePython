from math import *
a1, a2, a3, b1, b2, b3= map(int,input().split())
A = ceil((a1+ a2+ a3)/5)
B = ceil((b1+ b2+ b3)/10)
n = int(input())

if  (A+B)<=n:
    print('YES')
else : print ('NO')