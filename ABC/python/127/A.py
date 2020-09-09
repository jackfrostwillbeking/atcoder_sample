import sys
A,B = map(int,input().split())
if not ( 0 <= A <= 100 ): sys.exit()
if not ( 2 <= B <= 1000 ): sys.exit()
if not ( B % 2 == 0 ): sys.exit()

if A <= 5: print(0)
if 6 <= A <= 12: print(B//2)
if A >= 13: print(B)
 