import sys
i = input()
if not ( i.isupper() or i.islower() ): sys.exit()

if i.isupper(): print('A')
if i.islower(): print('a')