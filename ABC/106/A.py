import sys
A,B = map(int,input().split())
if not ( 2 <= A <= 100 and 2 <= B <= 100 ):
    sys.exit()

print(A * B - A - B + 1)