import sys
from collections import deque
import heapq

def input():
    return sys.stdin.readline().rstrip()
dx=[-1,0,0,1]
dy=[0,-1,1,0]

n,m,k=map(int,input().split())
arr=[]
target={}
for _ in range(n):
    arr.append(list(map(int,input().split())))
tx,ty=map(int,input().split())
tx,ty=tx-1,ty-1

for _ in range(m):
    a,b,c,d=map(int,input().split())
    arr[a-1][b-1]=2
    arr[c-1][d-1]=3
    target[(a-1,b-1)]=(c-1,d-1)
visited=[[False]*(n) for _ in range(n)]
ans=0

def find_guest(x,y):
    if (x,y) in target:
        nx,ny=target[(x,y)]
        del target[(x,y)]
        arr[x][y]=0
        return (x,y,nx,ny,0)
    q=deque([(x,y)])
    visited=[[False]*(n) for _ in range(n)]
    visited[x][y]=True
    res=[]
    cost=0
    while q:
        q_length=len(q)
        if len(res)>0:
            break
        for _ in range(q_length):
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if nx>=0 and nx<n and ny>=0 and ny<n and arr[nx][ny]!=1:
                    if visited[nx][ny]:
                        continue
                    if (nx,ny) in target:
                        heapq.heappush(res,(nx,ny))
                    else:
                        q.append((nx,ny))
                    visited[nx][ny]=True
        cost+=1
    if len(res)==0:
        return (-1,-1,-1,-1,10000000)
    guest_x,guest_y=heapq.heappop(res)
    dest_x,dest_y=target[(guest_x,guest_y)]
    del target[(guest_x,guest_y)]
    arr[guest_x][guest_y]=0
    return (guest_x,guest_y,dest_x,dest_y,cost)

def find_dest(x,y,dest_x,dest_y):
    q=deque([(x,y)])
    visited=[[False]*(n) for _ in range(n)]
    visited[x][y]=True
    cost=0
    found=False
    while q:
        if found:
            break
        q_length=len(q)
        cost+=1
        for _ in range(q_length):
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if nx>=0 and ny>=0 and nx<n and ny<n and arr[nx][ny]!=1:
                    if nx==dest_x and ny==dest_y:
                        found=True
                        break
                    if visited[nx][ny]:
                        continue
                    else:
                        q.append((nx,ny))
                    visited[nx][ny]=True
    arr[dest_x][dest_y]=0
    if found:
        return (dest_x,dest_y,cost)             
    else:
        return (-1,-1,100000000)
                

while m:
    guest_x,guest_y,dest_x,dest_y,cost=find_guest(tx,ty)
    k-=cost
    if k<=0:
        break
    tx,ty,cost=find_dest(guest_x,guest_y,dest_x,dest_y)
    if tx!=-1 and ty!=-1 and k-cost>=0:
        k=(k-cost)+2*cost
        m-=1
    else:
        break
            
if not m==0:
    print(-1)
else:
    print(k)