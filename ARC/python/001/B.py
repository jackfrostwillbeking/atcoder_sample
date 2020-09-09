import sys
A,B = map(int,input().split())
if not ( 0 <= A <= 40 and 0 <= B <= 40 ): sys.exit()

count = 0
diff = abs( B - A )
print(diff)
while diff > 0:
    if diff > 10:
        diff -= 10
        count += 1
    if 7 <= diff <= 8:
        diff -= diff
        count += 3
    if diff ==4 or diff == 6 or diff == 9:
        diff -= diff
        count += 2
    if diff == 5 or diff == 10:
        diff -= diff
        count += 1
    if diff <= 3:
        diff -= diff
        count += diff
print(count)