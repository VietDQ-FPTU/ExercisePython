import math
x, y = map(int, input().split())
temp = x
x = y
y = temp
print(128 * x + 97 * y + 1000)
