import sys
from collections import deque

def input():
    return sys.stdin.readline()

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n,m=map(int,input().split())
arr=[]
walls=[]
group={}
visited=[[False]*m for _ in range(n)]

for _ in range(n):
    string_list=list(input().rstrip())
    arr.append(list(map(int,string_list)))
    
idx=-1
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            walls.append((i,j))
        if arr[i][j]==0:
            q=deque([(i,j)])
            visited[i][j]=True
            arr[i][j]=idx
            cnt=1
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if nx>=0 and ny>=0 and nx<n and ny<m and not visited[nx][ny] and not arr[nx][ny]:
                        cnt+=1
                        q.append((nx,ny))
                        visited[nx][ny]=True      
                        arr[nx][ny]=idx
            group[idx]=cnt
            idx-=1  

for x,y in walls:
    hash={}
    cnt=1
    for k in range(4):
        nx,ny=x+dx[k],y+dy[k]
        if nx>=0 and ny>=0 and nx<n and ny<m and arr[nx][ny]<0 and not arr[nx][ny] in hash:
            cnt+=group[arr[nx][ny]]
            hash[arr[nx][ny]]=True
    arr[x][y]=cnt
    
for i in range(n):
    for j in range(m):
        if arr[i][j]<0:
            print(0,end='')
        else:
            print(arr[i][j]%10,end='')
    print()