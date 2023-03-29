import sys

def input():
    return sys.stdin.readline()
ans=[]

def dfs(root,prev):
    global cycle
    visited[root]=True
    for node in graph[root]:
        if node==prev:
            continue
        if visited[node]:
            cycle=True
            continue
        dfs(node,root)

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    graph=[[] for _ in range(n+1)]
    visited=[False]*(n+1)
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    cnt=0
    for i in range(1,n+1):
        cycle=False
        dfs(i,-1)
        if not cycle:
            cnt+=1
    ans.append(cnt)
for i,a in enumerate(ans):
    res="Case "+str(i+1)+": "
    if a>1:
        res+="A forest of "+str(a)+" trees."
    elif a==1:
        res+="There is one tree."
    else:
        res+="No trees."
    print(res)