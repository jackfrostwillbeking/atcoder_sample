import sys
N,X,T = map(int,input().split())

if not ( 1 <= N <= 1000 or 1 <= X <= 1000 or 1 <= T <= 1000 ): sys.exit()

print(N//X*T) if N%X == 0 else print((N//X*T)+T)