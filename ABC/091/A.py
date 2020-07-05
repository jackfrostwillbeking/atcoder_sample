import sys
A,B,C = map(int,input().split())
if not ( 1 <= A <= 500 and 1 <= B <= 500 ):
    sys.exit()
if not (1 <= C <= 1000):
    sys.exit()

print("Yes") if (A + B) >= C else print("No")
    