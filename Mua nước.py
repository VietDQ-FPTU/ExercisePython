x, y, z = map(int, input().split())
sum = 0
if y * 2 > z:
    sum = (x // 2) * z
    x = x % 2
    if x > 0:
        sum += y
else:
    sum = x * y
print(sum)
