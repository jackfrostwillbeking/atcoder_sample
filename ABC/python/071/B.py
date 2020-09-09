import sys
import string
S = str(input())
if len(S) < 1 or len(S) > 10 ** 5:
    sys.exit()
if not S.islower():
    sys.exit()

# array_a_to_z = [chr(ord('a') + i) for i in range(26)]
# for I in array_a_to_z:
for I in string.ascii_lowercase: #this is better?
    if I not in S:
        print(I)
        sys.exit()
print("None")