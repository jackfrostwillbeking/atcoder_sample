#Good question
import sys
import copy
N = input()
array = list(map(str,input().split()))

if not ( 3 <= N <= 10**5 ): sys.exit()

for I in range(len(array)):
    sample = copy.copy(array)
    sample[0] = 'S'
    sample[1] = 'S'
    for J in range(2,len(sample)+1):
        if array[J] == 'o':
            sample[J] == 'S'
        else
            sample[J] == 'W':
    if sample[-1] == 'S' and sample[-2] == ''
    SS
    WW
    SW
    WS