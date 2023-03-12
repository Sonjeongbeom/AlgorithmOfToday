import sys
from collections import Counter

S = sys.stdin.readline().rstrip()

for i in range(len(S)) :
    S = S.replace('00', '0')
    S = S.replace('11', '1')

counter = Counter(S)
if len(counter) == 1 :
    print(0)
else :
    print(min(counter.values()))