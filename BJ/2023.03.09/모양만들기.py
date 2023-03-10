import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n,m=map(int,input().split()) 

arr=[]
group={}
ans=0

for _ in range(n):
    arr.append(list(map(int,input().split())))

visited=[[0]*m for _ in range(n)]
idx=1

for i in range(n):
    for j in range(m):
        if arr[i][j]==1 and not visited[i][j]:
            idx+=1
            values=[(i,j)]
            value=1
            q=deque([(i,j)])            
            visited[i][j]=1
            arr[i][j]=idx
           
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if nx>=0 and ny>=0 and nx<n and ny<m and not visited[nx][ny] and arr[nx][ny]==1:
                        value+=1
                        visited[nx][ny]=1
                        arr[nx][ny]=idx
                        q.append((nx,ny))
            group[idx]=value
                    
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            hash={}
            value=1
            for k in range(4):
                nx,ny=i+dx[k],j+dy[k]
                if nx>=0 and ny>=0 and nx<n and ny<m and arr[nx][ny]>1 and arr[nx][ny] not in hash:
                    value+=group[arr[nx][ny]]
                    hash[arr[nx][ny]]=True
            ans=max(ans,value)
            
print(ans)