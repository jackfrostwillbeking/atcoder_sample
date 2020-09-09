import sys
N = int(input())
if N < 0 or N > 100:
    sys.exit()

max = 0
answer = 1
for I in reversed(range(N+1)):
    if I % 2 == 0:
        result = I
        count = 0
        for J in range(I):
            if result % 2 == 0:
                result = int(result/2)
                count += 1
            if max <= count:
                max = count
                answer = I
print(answer)