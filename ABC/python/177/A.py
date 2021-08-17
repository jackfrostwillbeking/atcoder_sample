import sys
D,T,S = map(int,input().split())
if not 1 <= D <= 10000: sys.exit()
if not 1 <= T <= 10000: sys.exit()
if not 1 <= S <= 10000: sys.exit()

print('Yes') if D - (S * T) <= 0 else print('No')