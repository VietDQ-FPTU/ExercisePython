x = input()
if 'a' <= x <= 'z':
    if  x == 'z':
        print('a')
    else:    
        print(chr(ord(x) + 1))
else:
    if x == 'Z':
        print('a')
    else:
        print(chr(ord(x) + 33))
