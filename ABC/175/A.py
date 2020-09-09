import sys
S = input()
setS = set(S)
if not ( len(S) == 3 ): sys.exit()
if not ( ('S' in setS and 'R' in setS and len(setS) == 2 ) or ( 'S' in setS and len(setS) == 1 ) or ( 'R' in setS and len(setS) == 1 )): sys.exit()

if 'RRR' == S: print(3);sys.exit()
if 'RR' in S: print(2);sys.exit()
if S == 'RSR' or S == 'SRS': print(1);sys.exit()
print(0)