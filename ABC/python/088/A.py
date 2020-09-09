import sys
N = int(input())
A = int(input())

if not (1 <= N <= 10000):
    sys.exit()
sys.exit() if not (0 <= A <= 1000) else ''

print('Yes') if (N % 500 <= A) else print('No')
    