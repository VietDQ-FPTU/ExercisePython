from math import *
x = int(input())
print('YES') if x % 2 == 0 else print('NO')
print('YES') if x % 3 == 0 and x % 5 == 0 else print('NO')
print('YES') if x % 3 == 0 and x % 7 != 0 else print('NO')
print('YES') if x % 3 == 0 or x % 7 == 0 else print('NO')
print('YES') if x > 30 and x < 50 else print('NO')
print('YES') if x >= 30 and (x % 2 == 0 or x % 3 == 0 or x % 5 == 0) else print('NO')
print('YES') if x >= 10 and x <= 99 and ((x % 10) in (2, 3, 5, 7)) else print('NO')
print('YES') if x <= 100 and x % 23 == 0 else print('NO')
print('YES') if x < 10 or x > 20 else print('NO')
print('YES') if (x % 10) in (0, 3 , 6, 9) else print('NO')
