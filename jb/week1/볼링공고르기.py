import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().rstrip().split())
counter = Counter(list(map(int, sys.stdin.readline().rstrip().split())))
answer = 0

for i in range(1, M) :
    N -= counter[i]
    answer += counter[i] * N
    
print(answer)

