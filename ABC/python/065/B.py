import sys
N = int(input())
if N < 1 or N > 10 ** 5:
    sys.exit()

int_array = []
for I in range(N):
    int_array.append(int(input()))
if len(int_array) < 0 or len(int_array) > N:
    sys.exit()

next = int_array[0]
count = 1
for L in range(N):
    if next == 2:
        print(count)
        sys.exit()
    next = int_array[next-1]
    count += 1
print("-1")