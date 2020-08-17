#Good question
import sys
import copy
import itertools
N,M = map(int,input().split())
check_list = [ a for a in range(N) ]
array = {}
for I in range(N):
    a,b = map(int,input().split())
    array.setdefault(a, []).append(b)
    array.setdefault(b, []).append(a)
# print(array)
# print(array[1])
array2 = copy.copy(array)
print(array2)
# list(itertools.product(A, B, C))
# next = 0
# array_hoge = []
# for J in range(1,N+1):
#     arrays = []
#     arrays.append(1)
#     for K in array[J]:
#         for L in range(len(array[J])):
#             print(K)
#             arrays[L]=arrays.append(K)
#         # array_hoge.append(array2[J].append(K))
#     print(arrays)
# print(arrays)
next = 1
arrays = []
arrays.append(str(1))
arrays.append(str(1))
print(arrays[-1])
count = 0

for I in range(1,len(array)):
    count = 0
    print("count="+str(count))
    for J in array[next]:
        # print(arrays[-count])
        arrays[-count] = str(arrays[-count]) + str(J)
        count += 1
print(arrays)

count = len(array) - 1
tmp_array = []
array_base = [1]
for I in range(1,len(array)):
    tmp_array += copy.copy(array_base)
    for J in range(1,len(array[I])+1):
        tmp_array += str(array[J])
        array_base += copy.copy(tmp_array)
#print(array_base)
print(*array2)
print(list(itertools.product(*array2)))