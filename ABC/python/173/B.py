import sys
N = int(input())
base = ['AC','WA','TLE','RE']
array = [ input() for a in range(N) ]

if not ( 1 <= N <= 10**5 ): sys.exit()
for I in array:
    if I not in base: sys.exit()

for I in base:
    print(I+' x '+str(array.count(I)))