import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
q=deque([n])
visited=[0]*(n+1)
prev=[0]*(n+1)

while q:
    now=q.popleft()
    if now==1:
        break
    if visited[now-1]==0:
        q.append((now-1))
        visited[now-1]=visited[now]+1
        prev[now-1]=now
    if now%2==0 and visited[now//2]==0:
        q.append((now//2))
        visited[now//2]=visited[now]+1
        prev[now//2]=now
    if now%3==0 and visited[now//3]==0:
        q.append((now//3))
        visited[now//3]=visited[now]+1
        prev[now//3]=now
    

print(visited[1])
res=[]
i=1
while i!=n:
    res.append(i)
    i=prev[i]
res.append(n)
res=res[::-1]
print(*res)
    