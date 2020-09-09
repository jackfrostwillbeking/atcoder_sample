import sys
S = input()
if len(S) != 10:
    sys.exit()
if S[0:8] != '2017/01/':
    print("ここ１")
    sys.exit()
if 1 <= int(S[-2:]) <= 31:
    print("ここ")
    sys.exit()

print(S.replace('2017','2018'))
