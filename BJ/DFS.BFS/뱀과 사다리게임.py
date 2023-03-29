import sys
from collections import deque

def input():
    return sys.stdin.readline()

arr=[0]*101
visited=[False]*110

n,m=map(int,input().split())
q=deque([(1,0)])
visited[1]=False
portal={}
for _ in range(n+m):
    a,b=map(int,input().split())
    portal[a]=b
ans=0
while q:
    now,dist=q.popleft()
    if now==100:
        ans=dist
        break
    for i in range(1,7):
        new=now+i
        if new in portal:
            q.append((portal[new],dist+1))
            visited[new]=False
        elif new<=100 and visited[new]==False:
            q.append((new,dist+1))
            visited[new]=True
print(ans)
