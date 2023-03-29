import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

t=int(input())
ans=[]
for _ in range(t):
    n,m=map(int,input().split())
    books={}
    for i in range(1,n+1):
        books[i]=True
    heap=[]
    cnt=0
    for _ in range(m):
        a,b=map(int,input().split())
        heapq.heappush(heap,(b,a))
    while heap:
        b,a=heapq.heappop(heap)
        for num in range(a,b+1):
            if books[num]:
                books[num]=False
                cnt+=1
                break
    ans.append(cnt)
    
for a in ans:
    print(a)
    