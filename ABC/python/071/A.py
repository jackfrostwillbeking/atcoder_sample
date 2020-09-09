import sys
x,a,b = map(int,input().split())
if x < 0 or a < 0 or b < 0 or x > 1000 or a > 1000 or b > 1000:
    sys.exit()

if abs(x-a) > abs(x-b):
    print("B")
if abs(x-a) < abs(x-b):
    print("A")
    