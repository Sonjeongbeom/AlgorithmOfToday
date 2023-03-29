import sys
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()

n=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(n):
    arr=list(map(int,input().split()))
    node=arr[0]
    for i in range(1,len(arr)-1,2):
        graph[node].append((arr[i],arr[i+1]))

mxNode,mxCost=0,0

def dfs(cur,dist):
    global mxNode,mxCost
    if mxCost<dist:
        mxNode=cur
        mxCost=dist
    for node,cur_dist in graph[cur]:
        if visited[node]:
            continue
        visited[node]=True
        dfs(node,dist+cur_dist)

visited[1]=True
dfs(1,0)
visited=[False]*(n+1)
visited[mxNode]=True
dfs(mxNode,0)
print(mxCost)