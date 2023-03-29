import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dir=[(0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
board=[]
across=[(-1,-1),(-1,1),(1,1),(1,-1)]

n,m=map(int,input().split())
clouds=[(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
for _ in range(n):
    board.append(list(map(int,input().split())))
    
ans=0

for _ in range(m):
    d,s=map(int,input().split())
    for i,cloud in enumerate(clouds):
        x,y=cloud
        dx,dy=dir[d]
        clouds[i]=(x+dx*s)%n,(y+dy*s)%n
    check=[]
    hash={}
    for x,y in clouds:
        board[x][y]+=1
        check.append((x,y))
        hash[(x,y)]=True
    clouds=[]
    for x,y in check:
        cnt=0
        for i in range(4):
            dx,dy=across[i]
            nx,ny=x+dx,y+dy
            if nx>=0 and ny>=0 and nx<n and ny<n and board[nx][ny]>0:
                cnt+=1
        board[x][y]+=cnt
    for i in range(n):
        for j in range(n):
            if board[i][j]>=2 and (i,j) not in hash:
                clouds.append((i,j))
                board[i][j]-=2
                
for i in range(n):
    for j in range(n):
        ans+=board[i][j]
print(ans)
        
    