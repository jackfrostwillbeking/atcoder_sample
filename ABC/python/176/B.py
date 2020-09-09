import sys
N = input()
if not (0 <= int(N) <= 10**200000): sys.exit()

res = 0
for I in range(len(N)):
    res += int(N[I])
print('Yes') if res % 9 == 0 else print('No')

