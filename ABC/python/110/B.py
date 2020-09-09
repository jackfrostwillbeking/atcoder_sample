import sys
N,M,X,Y = map(int,input().split())
array_x = list(map(int,input().split()))
array_y = list(map(int,input().split()))

if not ( 1 <= N <= 100 and 1 <= M <= 100 ): sys.exit()
if not ( -100 <= X <= 100 and -100 <= Y <= 100 ): sys.exit()
for I in array_x:
    if not ( -100 <= I <= 100 and array_x.count(I) == 1 and I != X): sys.exit()
for J in array_y:
    if not ( -100 <= J <= 100 and array_y.count(J) == 1 and J != Y): sys.exit()

# if min(array_y) - max(array_x) >= 1:
#     for K in range(max(array_x),min(array_y)+1):
#         if X < K <= Y and max(array_x) < K and min(array_y) >= K:
#             print('No War')
#             sys.exit()
# if min(array_x) - max(array_y) >= 1:
#     for L in range(max(array_y),min(array_x)+1):
#         if X < L <= Y and max(array_y) < L and min(array_x) >= L:
#             print('No War')
#             sys.exit()

for I in range(X+1,Y+1):
    print(I)
    if I > max(array_x) and I <= min(array_y):
        print('No War')
        sys.exit()
print('War')