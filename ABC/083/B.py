import sys
N,A,B = map(int,input().split())

if not (1 <= N <= 10000 and 1 <= A <= 36 and 1 <= B <= 36):
    sys.exit()

sum = 0
for I in range(1,N+1):
    tmp = list(str(I))
    check = 0
    for J in range(len(tmp)):
        check += int(tmp[J])
    if A <= check <= B:
        sum += I
print(sum)
