import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

t=int(input())
res=[]

for _ in range(t):
    ans=0
    n,k=map(int,input().split())
    times=[0]
    times.extend(list(map(int,input().split())))
    prev_times=[0]*(n+1)
    indegree=[0]*(n+1)
    graph=[[] for _ in range((n+1))]
    for _ in range(k):
        a,b=map(int,input().split())
        graph[a].append(b)
        indegree[b]+=1
    w=int(input())
    q=deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now=q.popleft()
        if now==w:
            break
        for i in graph[now]:
            indegree[i]-=1
            prev_times[i]=max(prev_times[i],times[now])
            if indegree[i]==0:
                times[i]+=prev_times[i]
                q.append((i))
    res.append(times[w])       
    
for r in res:
    print(r)