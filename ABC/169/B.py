import sys
N = int(input())
array = list(map(int,input().split()))

if not ( 2 <= N <= 10**5 ): sys.exit()
if not ( 0 <= min(array) and max(array) <= 10**18): sys.exit()
if 0 in array: print(0); sys.exit()

sum = array[0]
for I in range(1,len(array)):
    sum *= array[I]
    if sum > 10**18: print(-1);sys.exit()
print(sum)