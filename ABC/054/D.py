#Good question
import sys
import itertools

N,Ma,Mb = map(int,input().split())
array = [ list(map(int,input().split())) for a in range(N) ]

budget = N * 100
for I in range(1,N+1):
    for K in list(itertools.combinations(array,I)):
        a = 0
        b = 0
        c = 0
        for L in K:
            a += L[0]
            b += L[1]
            c += L[2]
        if a/b == Ma/Mb and budget >= c: budget = c
print(budget) if budget != N * 100 else print(-1)