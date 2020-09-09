import sys
N,D = map(int,input().split())
# array = [ I for I in map(int,input().split()) ]
array = [ list(map(int,input().split())) for I in range(N) ]
print(array)
count = 0
for I in array:
    print(I)
    if (I[0]**2+I[1]**2)**(1/2) <= D:
        count += 1
# for I in range(N):
#     X,Y = map(int,input().split())
#     if (X**2+Y**2)**(1/2) <= D:
#         count += 1
print(count)