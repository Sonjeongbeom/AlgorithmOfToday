import sys

def input():
    return sys.stdin.readline().rstrip()

n,m=map(int,input().split())

visited=[[0]*m for _ in range(n)]

x,y,d=map(int,input().split())
arr=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for _ in range(n):
    arr.append(list(map(int,input().split(' '))))

visited[x][y]=1

count=1
turn=0
while True:
    d-=1
    if d==-1:
        d=3
    nx,ny=x+dx[d],y+dy[d]
    if visited[nx][ny]==0 and arr[nx][ny]==0:
        visited[nx][ny]=1
        x,y=nx,ny
        count+=1
        turn=0
        continue
    else:
        turn+=1
        if turn==4:
            nx,ny=x-dx[d],y-dy[d]
            if arr[nx][ny]==0:
                x,y=nx,ny
            else:
                break
            turn=0
            
print(count)
    
    
            
    
    
