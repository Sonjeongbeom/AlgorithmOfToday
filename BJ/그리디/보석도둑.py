import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

n,k=map(int,input().split())
jew=[]
bags=[]

for _ in range(n):
    m,v=map(int,input().split())
    jew.append((m,v))
for _ in range(k):
    c=int(input())
    bags.append(c)
bags.sort()
heapq.heapify(jew)

tmp_jew=[]
ans=0
for k in bags:
    while jew and jew[0][0]<=k:
        heapq.heappush(tmp_jew,-heapq.heappop(jew)[1])
    if tmp_jew:
        ans-=heapq.heappop(tmp_jew)
print(ans)