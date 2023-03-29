import sys
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()

n=int(input())

graph=[[] for _ in range(n+1)]
parents=[0]*(n+1)
parents[1]=1

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(i):
    for node in graph[i]:
        if parents[node]==0:
            parents[node]=i
            dfs(node)

dfs(1)

for i in range(2,len(parents)):
    print(parents[i])
    

