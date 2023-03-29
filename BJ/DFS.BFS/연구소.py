import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n,m=map(int,input().split())
ans=0
board=[]
safe=[]
virus=[]

for _ in range(n):
    board.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            safe.append((i,j))
        if board[i][j]==2:
            virus.append((i,j))
            
def bfs(arr):
    tmp=[]
    for value in arr:
        i,j=value
        board[i][j]=1
    q=deque([v for v in virus])
    visited=[[False]*(m) for _ in range(n)]
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<m and not visited[nx][ny] and board[nx][ny]==0:
                visited[nx][ny]=True
                board[nx][ny]=2
                tmp.append((nx,ny))
                q.append((nx,ny))
    cnt=0  
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                cnt+=1
            
    for i,j in arr:
        board[i][j]=0
    for i,j in tmp:
        board[i][j]=0
        
    return cnt
            
def dfs(arr,idx):
    global ans
    if len(arr)==3:
        ans=max(ans,bfs(arr))
        return
    
    for i in range(idx,len(safe)):
        s=safe[i]
        if s not in arr:
            dfs(arr+[s],i)
            
dfs([],0)
print(ans)