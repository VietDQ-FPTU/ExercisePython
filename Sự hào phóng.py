c1,c2,c3,c4,c5= map(int,input().split())
if  (c1 + c2 + c3 + c4 + c5) / 5 != 0 :
    if (c1 + c2 + c3 + c4 + c5) % 5 == 0: 
        print (int((c1 + c2 + c3 + c4 + c5)/5))
    else : print (-1)
else : print (-1)