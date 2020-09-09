import sys
X,Y = map(int,input().split())
if X < 0:
  sys.exit()
if Y > 1000000000:
  sys.exit()
  
if X - Y > 0:
  print(X)
elif X - Y < 0:
  print(Y)
else:
  print(X)
