import sys

def input():
    return sys.stdin.readline().rstrip()

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m=map(int,input().split())
board=[]
x,y,d=map(int,input().split())

for _ in range(n):
    board.append(list(map(int,input().split())))
    
ans=0
    
while True:
    if board[x][y]==0:
        board[x][y]=2
        ans+=1
    check=False
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<m and board[nx][ny]==0:
            check=True
    if not check:
        x-=dx[d]
        y-=dy[d]
        if nx<0 or ny<0 or nx>=n or ny>=m or board[x][y]==1:
            break
    else:
        d-=1
        if d<0:
            d=3
        nx,ny=x+dx[d],y+dy[d]
        if board[nx][ny]==0:
            x,y=nx,ny 
    
print(ans)
    