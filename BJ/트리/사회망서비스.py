import sys
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()

n=int(input())
graph=[[] for _ in range(n+1)]
dp=[[0]*2 for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(root):
    visited[root]=True
    dp[root][0]=0
    dp[root][1]=1
    
    for node in graph[root]:
        if visited[node]:
            continue
        dfs(node)
        dp[root][0]+=dp[node][1]
        dp[root][1]+=min(dp[node][1],dp[node][0])
        
dfs(1)
print(min(dp[1][0],dp[1][1]))