x = input()
if 'a' <= x <= 'z':
    print('LOWER')
elif 'A' <= x <= 'Z':
    print('UPPER')
elif '0' <= x <= '9':
    print('DIGIT')
else:
    print('SPECIAL')
