import sys

def input():
    return sys.stdin.readline().rstrip()

data=input()

alpha=''
number=0

for ch in data:
    if ch.isalpha():
        alpha+=ch
    else:
        number+=int(ch)

sortedCh=sorted(alpha)
print(''.join(sortedCh)+str(number))