import sys
N = int(input())

if not (1 <= N <= 10**3): sys.exit()

res = 1
for J in range(1,N+1):
    res *= J
print(res)
count = 0
for I in range(1,int(res*(1/2)+1)):
    if res % I == 0:
        print(I)
        count += 1
print(count+1)