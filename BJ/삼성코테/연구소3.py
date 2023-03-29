import sys
from collections import deque
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

dx=[1,0,-1,0]
dy=[0,1,0,-1]

board=[]
virus=[]
empty=0

ans=99999

n,m=map(int,input().split())

for _ in range(n):
    board.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(n):
        if board[i][j]==2:
            virus.append((i,j))
        if board[i][j]==0:
            empty+=1
active=list(combinations(virus,m))

def bfs(virus):
    global empty
    tmpEmpty=empty
    q=deque(virus)
    tmp=[]
    visited=[[False]*n for _ in range(n)]
    cnt=0
    if tmpEmpty==0:
        return cnt
    while q:        
        length=len(q)
        for _ in range(length):
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if nx>=0 and ny>=0 and nx<n and ny<n and not visited[nx][ny] and board[nx][ny]!=1:
                    if board[nx][ny]==0:
                        tmpEmpty-=1
                        tmp.append((nx,ny))
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    board[nx][ny]=2
        cnt+=1
        if tmpEmpty==0:
            break

    for i in range(n):
        for j in range(n):
            if board[i][j]==0:  
                for x,y in tmp:
                    board[x][y]=0
                return 99999
    for x,y in tmp:
        board[x][y]=0
        
    return cnt
    
for a in active:
    ans=min(ans,bfs(list(a)))

if ans==99999:
    print(-1)
else:
    print(ans)