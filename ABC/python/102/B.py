import sys
N = int(input())
array_A = list(map(int,input().split()))

if not (2 <= N <= 100):
    sys.exit()
for I in range(len(array_A)):
    if not (1 <= array_A[I] <= 10 ** 9):
        sys.exit()

print(max(array_A) - min(array_A))