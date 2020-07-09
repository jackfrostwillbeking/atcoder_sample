N,T = map(int,input().split())
array = []
array = [ [lista for lista in map(int,input().split())] for I in range(N) ]

m = 1001
for I in array:
    if I[1] > T:
        continue
    elif I[1] <= T:
        if I[0] < m: m = I[0]
print([m,'TLE'][m>1000])

# print(min) if min < 1001 else print('TLE')