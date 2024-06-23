x = int(input())
a, b = 0, 0 
if x >= 365:
    a = x // 365
    x -= 365 * (x // 365)
if x >= 7:
    b = x // 7
    x -= 7 * (x // 7)
print(a, b, x)
