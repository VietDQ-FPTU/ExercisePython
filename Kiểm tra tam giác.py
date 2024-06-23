a, b, c= map(float, input().split())
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a == b and b==c :
            print(1)
        elif a==b or b==c or a==c :
            print(2)
        elif  a*a+b*b==c*c or c*c+b*b==a*a or c*c+a*a==b*b :
            print(3)
        else :
            print(4)
    else:
        print('INVALID')
else:
    print('INVALID')
   
#vietNgu
