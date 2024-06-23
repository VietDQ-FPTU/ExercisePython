n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s1 = set(a)
s2 = set(b)
u = list(s1 & s2)
for i in a:
    if i in u:
        print(i,end = ' ')
        u.remove(i)