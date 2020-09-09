import sys
N = int(input())
array = list(map(int,input().split()))
sys.exit() if not (1 <= N <= 100) else ''
for I in range(len(array)):
    sys.exit() if not (1 <= array[I] <= 100) else ''

array.sort(reverse=True)
alice = 0
bob = 0
for J in range(len(array)):
    if J == 0 or J % 2 == 0:
        alice += array[J]
    else:
        bob += array[J]

print(alice - bob)