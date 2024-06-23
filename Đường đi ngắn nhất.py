from math import *
d1, d2, d3 = map(int,input().split())
C1= d1+d2+d3
C2= 2*(d1+d3)
C3= 2*(d1+d2)
C4= 2*(d2+d3)
print(min({C1,C2,C3,C4}))