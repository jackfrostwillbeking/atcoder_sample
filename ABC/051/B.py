import sys
K,S = map(int,input().split())
if K < 2 or K > 2500:
  sys.exit()

X = 0
count = 0
while X <= K:
  Y = 0
  while Y <= K:
    Z = S - X - Y
    if Z <= K and Z >= 0:
      count += 1
    Y += 1
  X += 1
print(count)