import sys
import re
S = input()
if not ( 1 <= len(S) <= 10 ): sys.exit()
if not S.isupper: sys.exit()

result = 0
max = max(re.findall('[A|T|G|C]+', S),key=len) if re.findall('[A|T|G|C]+', S) else ''
if len(max) > 0:result = len(max)
print(result)