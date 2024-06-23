x, y, z, t = map(float, input().split())
adv = (x + y + z * 2 + t * 3) / 7
if adv >= 8:
    print('GIOI')
elif 6.5 <= adv < 8:
    print('KHA')
elif 5 <= adv < 6.5:
    print('TRUNG BINH')
else:
    print('YEU')
