import sys
N,K,M = map(int,input().split())
array = list(map(int,input().split()))

if not ( 1 <= K <= 100 and 1 <= M <= K and 0 <= min(array) and max(array) <= K ): sys.exit()

x = N*M - sum(array)
if x < 0: x = 0
print(x) if x <= K else print(-1) 