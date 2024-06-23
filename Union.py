n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s1 = set(a)
s2 = set(b)
u = list(s1 | s2)
u.sort(reverse= True )
for i in u:
    print(i,end = ' ')