import sys
N = int(input())
string = input()
if not ( 1 <= N <= 100 ): sys.exit()
if not ( len(string) == N ): sys.exit()

max = string.count("1")
min = string.count("1")
for I in range(2,5):
    if string.count(str(I)) > max: max = string.count(str(I))
    if string.count(str(I)) < min: min = string.count(str(I))
print(str(max)+" "+str(min))