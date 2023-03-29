import sys
from collections import deque
import math

def input():
    return sys.stdin.readline().rstrip()

dx=[1,0,-1,0]
dy=[0,1,0,-1]


n,l,r=map(int,input().split())

board=[]

for _ in range(n):
    board.append(list(map(int,input().split())))

cnt=0
while True:
    check=False
    visited=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q=deque([(i,j)])
                visited[i][j]=1
                tmp=[]
                value=0
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if nx>=0 and ny>=0 and nx<n and ny<n and not visited[nx][ny]:
                            if l<=abs(board[x][y]-board[nx][ny])<=r:
                                check=True
                                tmp.append((nx,ny))
                                q.append((nx,ny))
                                visited[nx][ny]=1
                                value+=board[nx][ny]
                if value>0:
                    tmp.append((i,j))
                    value+=board[i][j]
                    value=math.floor(value//len(tmp))
                    for x,y in tmp:
                        board[x][y]=value       
    if check:
        cnt+=1
    else:
        break
    
print(cnt)
                    
    