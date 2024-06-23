from math import*
n = int(input())
print(floor(n/100)+floor((n-floor(n/100)*100)/20)+floor((n-floor(n/20)*20)/10)+floor((n-floor(n/10)*10)/5+floor((n-floor(n/5)*5)/1)))