import sys
A,B = map(int,input().split())
if not ( -100 <= A <= 100 and -100 <= B <= 100 ): sys.exit()

array = [ A+B, A-B, A*B ]
print(max(array))