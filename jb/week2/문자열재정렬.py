import sys

S = sys.stdin.readline().rstrip()

result = []
num = 0

for s in S :
    if s.isdigit() :
        num += int(s)
    else :
        result.append(s)
result.sort()

if num == 0 :
    print(''.join(result))
else :
    print(''.join(result) + str(num))