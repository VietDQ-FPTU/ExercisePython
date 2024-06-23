x, y, z, t = map(int, input().split())
sum = 0
min1 = min(x, z, t)
sum += 256 * min1
x, z, t = x - min1, z - min1, t - min1 
min2 = min(x, y)
sum += 32 * min2
print(sum)
