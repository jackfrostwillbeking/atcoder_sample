import sys
D,N = map(int,input().split())

if D not in [0,1,2] or not (1 <= N <= 100):
    sys.exit()

if N == 100:
    N += 1
print(N*(100**D))