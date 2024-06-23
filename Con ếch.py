from math import *
a, b, n = map(int,input().split())
if(n%2==0):
    print(int((a-b)*n/2))
elif(n%2==1):
    print(int(ceil(n/2)*a-floor(n/2)*b))