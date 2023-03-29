import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n,k=map(int,input().split())

arr=[]

for _ in range(n):
    arr.append(list(map(int,input().split())))

s,X,Y=map(int,input().split())

tmp=[]

for i in range(n):
    for j in range(n):
        if arr[i][j]!=0:
            tmp.append((arr[i][j],i,j))
tmp.sort()        
q=deque(tmp)

for _ in range(s):
    if not q:
        break
    length=len(q)
    for _ in range(length):
        virus,x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<n and not arr[nx][ny]:
                arr[nx][ny]=virus
                q.append((virus,nx,ny))
                      

print(arr[X-1][Y-1])