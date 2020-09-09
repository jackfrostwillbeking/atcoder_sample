import sys
import itertools
N = int(input())
array = list(map(int,input().split()))
setarray = set(array)
array = list(setarray)
count = 0
for I in itertools.combinations(array,3):
    setI = set(I)
    print(setI)
    if len(setI) != 3:continue
    count += 1
print(count)