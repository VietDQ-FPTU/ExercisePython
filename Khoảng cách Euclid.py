from math import *
x, y, z, t = map(int, input().split())
print('%.2f' % sqrt(pow((z - x), 2) + pow((t - y), 2)))
