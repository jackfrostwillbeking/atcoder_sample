import sys
N = int(input())
array = list(map(int,input().split()))

if not (1 <= N <= 2*(10**5)): sys.exit()
for I in array:
    if not ( 1 <= I <= 10**9 ): sys.exit()

sum = 0
max = 0
for J in array:
    if J < max:
        sum += max - J
    else:
        max = J
print(sum)