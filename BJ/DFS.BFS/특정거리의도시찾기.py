import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n,m,k,x=map(int,input().split())

graph=[[] for _ in range(n+1)]

visited=[0]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    
q=deque([(0,x)])
visited[x]=True

ans=[]

while q:
    dist,now=q.popleft()
    if dist==k:
        ans.append(now)
    for node in graph[now]:
        if visited[node]==False:
            visited[node]=True
            q.append((dist+1,node))

ans.sort()
if len(ans)==0:
    print(-1)
for value in ans:
    print(value)
            