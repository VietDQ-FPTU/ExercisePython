n = int(input())
a = list(map(int,input().split()))
s = set(a)
q = int(input())
for i in range (0,q):
    x = int(input())
    if x in s: print('YES')
    else: print('NO')