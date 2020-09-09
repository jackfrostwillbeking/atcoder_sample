import sys
N,M = map(int,input().split())
A = []
B = []
for I in range(N):
    A += list(map(str,input().split()))
for J in range(M):
    B += list(map(str,input().split()))

if N < 0 or M < 0 or N > 50 or M > 50 or N < M:
    sys.exit()
print(A)
print(B)

if list(set(A) & set(B)) == B:
    print("Yes")
else:
    print("No")
