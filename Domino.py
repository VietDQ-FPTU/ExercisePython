x, y = map(int, input().split())
sum = 0
if x % 2 == 0:
    sum += (x // 2) * y
else:
    sum += (x // 2) * y + (y // 2)
print(sum)
