from math import *
n, S = map(int,input().split())
if(S==0):
    print(0)
elif(S==n):
    print (1)
elif(S%n==0):
    print(int(S/n))
elif(S%n!=0):
    print(int(S/n)+1)