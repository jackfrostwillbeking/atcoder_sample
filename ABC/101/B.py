N = input()
array_N = [int(I) for I in list(N)]
N = int(N)

print('Yes') if N % sum(array_N) == 0 else print('No')