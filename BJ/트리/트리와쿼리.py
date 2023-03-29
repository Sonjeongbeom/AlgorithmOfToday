import sys
sys.setrecursionlimit(10**5)

def input():
    return sys.stdin.readline()

n,r,q=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
sub_nodes=[0]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i):
    visited[i]=True
    cur=1
    for node in graph[i]:
        if not visited[node]:
            cur+=dfs(node)
    sub_nodes[i]=cur
    return cur
dfs(r)
ans=[]
for _ in range(q):
    root=int(input())
    ans.append(sub_nodes[root])
    
for a in ans:
    print(a)