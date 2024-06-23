h,m = map(int, input().split())
p = 24*60
if 0<= h < 24  and 0<= m<60:
    print(p-(h*60+m))
else :
    print('INVALID')