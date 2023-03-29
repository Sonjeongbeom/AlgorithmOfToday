import sys
sys.setrecursionlimit(10**5)

def input():
    return sys.stdin.readline()

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

def dfs(root,prev):
    global cycle
    visited[root]=True
    for node in graph[root]:
        if prev==node:
            continue
        if visited[node]:
            cycle+=1
            continue
        dfs(node,root)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cycle_cnt=0
component=0
for i in range(1,n+1):
    cycle=0
    if not visited[i]:
        dfs(i,-1)
        component+=1
        if cycle:
            cycle_cnt+=cycle//2
print(component-1+cycle_cnt)