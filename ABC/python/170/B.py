import sys
X,Y = map(int,input().split())

if not ( 1 <= X <= 100 and 1 <= Y <= 100 ): sys.exit()

for I in range(101):
    for J in range(101):
        if (I*2 + J*4) == Y and I+J == X:
            print('Yes')
            sys.exit()
print('No')