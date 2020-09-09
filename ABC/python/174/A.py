import sys
X = int(input())
if not ( -40 <= X <= 40 ): sys.exit()

print('Yes') if X >= 30 else print('No')