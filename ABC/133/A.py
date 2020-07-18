import sys
N,A,B = map(int,input().split())

if not ( 1 <= N <= 20 and 1 <= A <= 50 and 1 <= B <= 50 ): sys.exit()

print( N * A ) if ( N * A ) <= B else print(B)