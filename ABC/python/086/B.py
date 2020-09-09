import sys
import math

a,b = map(int,input().split())
if not (1 <= a <= 100 and 1 <= b <= 100):
    sys.exit()

result = math.sqrt(int(str(a)+str(b))).is_integer()
print('Yes') if result == True else print('No')
    