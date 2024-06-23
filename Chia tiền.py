from math import *
a,b,c,n= map(int,input().split())
t = a + b+ c + n
if  1<=a and 1<= b and 1<= c and 1<= n:
    if (t) % 3 == 0: 
        if(abs(a-t/3)+abs(b-t/3)+abs(c-t/3))<=n:
            print('YES')
        else: print('NO')
    else : print ('NO')